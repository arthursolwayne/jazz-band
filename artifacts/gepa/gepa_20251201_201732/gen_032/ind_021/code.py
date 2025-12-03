
import pretty_midi

# Create the MIDI file with 160 BPM (4/4 time)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Dante on tenor sax
bass = pretty_midi.Instrument(program=33)      # Marcus on bass
piano = pretty_midi.Instrument(program=0)      # Diane on piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray on drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1 (0.0 - 1.5s)
drum_notes = [
    (0.0, 36),  # Kick on beat 1
    (0.375, 42),  # Hihat on beat 1 & 2
    (0.75, 38),  # Snare on beat 2
    (1.125, 42),  # Hihat on beat 3
    (1.5, 36),  # Kick on beat 3
    (1.875, 42),  # Hihat on beat 3 & 4
    (2.25, 38),  # Snare on beat 4
    (2.625, 42),  # Hihat on beat 4
]

for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif - F (G5), A (Bb5), Bb (C5), D (Eb5)
# These are the first four notes of your melody: F, A, Bb, D
# Phrased as a rhythm: long, short, short, long (on beat 1, 2, 3, 4)

sax_notes = [
    (1.5, 71, 0.5),  # F (G5)
    (2.0, 73, 0.25),  # A (Bb5)
    (2.25, 72, 0.25),  # Bb (C5)
    (2.75, 76, 0.25),  # D (Eb5)
]

for start, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# Bass: walking line with chromatic approaches - F (E2), G (F2), Ab (Gb2), Bb (Ab2), F (E2)
# Roots and fifths, approaching on the upbeats

bass_notes = [
    (1.5, 57, 0.5),  # F (E2) - root
    (1.75, 58, 0.25),  # G (F2) - chromatic approach
    (2.0, 59, 0.5),  # Ab (Gb2) - fifth
    (2.25, 60, 0.25),  # Bb (Ab2) - chromatic approach
    (2.5, 57, 0.5),  # F (E2) - root
]

for start, pitch, duration in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: open voicings, different chord each bar, resolve on the last

# Bar 2: F7 (op13) - F, A, C, E (root, 3, 5, b7)
piano_notes = [
    (1.5, 71, 0.5),  # F (G5)
    (1.5, 73, 0.5),  # A (Bb5)
    (1.5, 76, 0.5),  # C (Eb5)
    (1.5, 78, 0.5),  # E (F5)
]

for start, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Bar 3: Gm7 (op11) - G, Bb, D, F
piano_notes = [
    (3.0, 74, 0.5),  # G (A5)
    (3.0, 73, 0.5),  # Bb (Bb5)
    (3.0, 77, 0.5),  # D (F5)
    (3.0, 76, 0.5),  # F (Eb5)
]

for start, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Bar 4: Bb7 (op13) - Bb, D, F, Ab
piano_notes = [
    (4.5, 73, 0.5),  # Bb (Bb5)
    (4.5, 77, 0.5),  # D (F5)
    (4.5, 76, 0.5),  # F (Eb5)
    (4.5, 75, 0.5),  # Ab (Db5)
]

for start, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Same pattern as Bar 1, repeating the kick-snare-hihat rhythm

for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (start, 36),  # Kick on beat 1
        (start + 0.375, 42),  # Hihat on beat 1 & 2
        (start + 0.75, 38),  # Snare on beat 2
        (start + 1.125, 42),  # Hihat on beat 3
        (start + 1.5, 36),  # Kick on beat 3
        (start + 1.875, 42),  # Hihat on beat 3 & 4
        (start + 2.25, 38),  # Snare on beat 4
        (start + 2.625, 42),  # Hihat on beat 4
    ]

    for start_time, note in drum_notes:
        drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=start_time + 0.125)
        drums.notes.append(drum_note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
