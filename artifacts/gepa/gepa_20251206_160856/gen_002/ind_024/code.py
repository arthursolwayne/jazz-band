
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.375, 42, 100), # Hihat on 2
    (0.75, 38, 100),  # Snare on 3
    (1.125, 42, 100), # Hihat on 4
    (1.5, 36, 100)    # Kick on 1 of next bar
]
for start, note, velocity in drum_notes:
    drum_note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

# Bar 2: Full quartet starts here (1.5 - 3.0s)
# Bass: F2 (D2 is the root of Fm?), walking line starting on F2 (MIDI 53), chromatic approach
bass_notes = [
    (1.5, 53, 100),  # F2
    (1.875, 54, 100), # F#2 (chromatic approach)
    (2.25, 51, 100),  # D2 (fifth)
    (2.625, 53, 100), # F2
]
for start, note, velocity in bass_notes:
    bass_note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Piano: Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    (1.5, 53, 100),  # F
    (1.5, 60, 100),  # C
    (1.5, 64, 100),  # Eb
    (1.5, 66, 100),  # Ab
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (2.25, 58, 100),  # Bb
    (2.25, 62, 100),  # D
    (2.25, 53, 100),  # F
    (2.25, 66, 100),  # Ab
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (3.0, 60, 100),   # C
    (3.0, 64, 100),   # Eb
    (3.0, 67, 100),   # G
    (3.0, 66, 100)    # Ab
]
for start, note, velocity in piano_notes:
    piano_note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(piano_note)

# Drums: Bar 2 (1.5 - 3.0s)
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (1.875, 42, 100), # Hihat on 2
    (2.25, 38, 100),  # Snare on 3
    (2.625, 42, 100), # Hihat on 4
    (3.0, 36, 100),   # Kick on 1 of next bar
]
for start, note, velocity in drum_notes:
    drum_note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

# Sax: Your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F, Ab, Bb, C (in 4 notes)
# Start at 1.5s, end at 2.25s (leaving it hanging), come back at 3.0s
sax_notes = [
    (1.5, 53, 100),   # F
    (1.875, 64, 100),  # Ab
    (2.25, 62, 100),  # Bb (leave it hanging)
    (3.0, 60, 100),   # C (come back and finish it)
]
for start, note, velocity in sax_notes:
    sax_note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(sax_note)

# Bar 3: Drums (3.0 - 4.5s)
drum_notes = [
    (3.0, 36, 100),  # Kick on 1
    (3.375, 42, 100), # Hihat on 2
    (3.75, 38, 100),  # Snare on 3
    (4.125, 42, 100), # Hihat on 4
    (4.5, 36, 100)    # Kick on 1 of next bar
]
for start, note, velocity in drum_notes:
    drum_note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

# Bar 3: Bass
bass_notes = [
    (3.0, 51, 100),  # D2 (fifth)
    (3.375, 53, 100), # F2
    (3.75, 54, 100),  # F#2 (chromatic approach)
    (4.125, 51, 100), # D2
]
for start, note, velocity in bass_notes:
    bass_note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Bar 3: Piano
piano_notes = [
    (3.0, 58, 100),  # Bb
    (3.0, 62, 100),  # D
    (3.0, 53, 100),  # F
    (3.0, 66, 100),  # Ab
]
for start, note, velocity in piano_notes:
    piano_note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(piano_note)

# Bar 4: Drums (4.5 - 6.0s)
drum_notes = [
    (4.5, 36, 100),  # Kick on 1
    (4.875, 42, 100), # Hihat on 2
    (5.25, 38, 100),  # Snare on 3
    (5.625, 42, 100), # Hihat on 4
]
for start, note, velocity in drum_notes:
    drum_note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

# Bar 4: Bass
bass_notes = [
    (4.5, 53, 100),  # F2
    (4.875, 54, 100), # F#2 (chromatic approach)
    (5.25, 51, 100),  # D2 (fifth)
    (5.625, 53, 100)  # F2
]
for start, note, velocity in bass_notes:
    bass_note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Bar 4: Piano
piano_notes = [
    (4.5, 60, 100),   # C
    (4.5, 64, 100),   # Eb
    (4.5, 67, 100),   # G
    (4.5, 66, 100)    # Ab
]
for start, note, velocity in piano_notes:
    piano_note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(piano_note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
