
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Saxophone
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
drum_kick = 36
drum_snare = 38
drum_hihat = 42

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=drum_kick, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=drum_snare, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=drum_hihat, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)
# Bars 2-4 = 1.5 to 6.0s, 3 bars total

# Bass line: Marcus, walking line with chromatic approach
bass_notes = [
    (1.5, 59),  # Fm7 - F
    (1.875, 60), # Bb
    (2.25, 58),  # Eb
    (2.625, 60), # G
    (3.0, 59),   # F
    (3.375, 60), # Bb
    (3.75, 58),  # Eb
    (4.125, 60), # G
    (4.5, 59),   # F
    (4.875, 60), # Bb
    (5.25, 58),  # Eb
    (5.625, 60), # G
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: Diane, 7th chords on 2 and 4, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bbm7 = Bb, Db, F, Ab
# Chord on beat 2 and 4 of each bar

# Bar 2
piano_notes = [
    (2.25, 79),   # F (C4)
    (2.25, 76),   # Ab
    (2.25, 72),   # C
    (2.25, 71),   # Eb
    (3.0, 77),    # Bb
    (3.0, 74),    # Db
    (3.0, 79),    # F
    (3.0, 76),    # Ab
    (4.5, 79),    # F
    (4.5, 76),    # Ab
    (4.5, 72),    # C
    (4.5, 71),    # Eb
    (5.25, 77),   # Bb
    (5.25, 74),   # Db
    (5.25, 79),   # F
    (5.25, 76),   # Ab
]

for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.125)
    piano.notes.append(note)

# Sax: Dante, melody (Fm scale, but with tension and release)
# Motif: F - Ab - Eb (with a space between Eb and F), then resolve
# Bar 2: F (start), Ab (beat 2), Eb (beat 3), F (beat 4)
# Bar 3: leave it hanging, then resolve in bar 4

sax_notes = [
    (1.5, 79),   # F (C4)
    (1.875, 76), # Ab
    (2.25, 71),  # Eb
    (2.625, 79), # F
    (3.0, 79),   # F (sustain, tie into next bar)
    (3.375, 76), # Ab
    (3.75, 71),  # Eb
    (4.125, 79), # F
    (4.5, 79),   # F
    (4.875, 76), # Ab
    (5.25, 71),  # Eb
    (5.625, 79)  # F
]

for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
