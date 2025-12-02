
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Drums in Bar 1
drum_notes = [
    (0.0, 36, 100),  # Kick on beat 1
    (0.75, 42, 100), # Hihat on &1
    (1.0, 38, 100),  # Snare on beat 2
    (1.5, 36, 100),  # Kick on beat 3
    (2.25, 42, 100), # Hihat on &3
    (2.5, 38, 100)   # Snare on beat 4
]
for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    drums.notes.append(dr)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in C
bass_notes = [
    (1.5, 60, 80),  # C4
    (1.75, 61, 80), # D4
    (2.0, 63, 80),  # E4
    (2.25, 62, 80), # D4
    (2.5, 60, 80),  # C4
    (2.75, 61, 80), # D4
    (3.0, 63, 80),  # E4
    (3.25, 62, 80), # D4
    (3.5, 60, 80),  # C4
    (3.75, 61, 80), # D4
    (4.0, 63, 80),  # E4
    (4.25, 62, 80), # D4
    (4.5, 60, 80),  # C4
    (4.75, 61, 80), # D4
    (5.0, 63, 80),  # E4
    (5.25, 62, 80)  # D4
]
for time, note, velocity in bass_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano (Diane) - 7th chords on 2 & 4 (C7, F7, Bb7, E7)
piano_notes = [
    # Bar 2
    (2.0, 60, 100), # C
    (2.0, 64, 100), # E
    (2.0, 67, 100), # G
    (2.0, 71, 100), # B
    # Bar 3
    (3.5, 65, 100), # F
    (3.5, 69, 100), # A
    (3.5, 72, 100), # C
    (3.5, 76, 100), # D#
    # Bar 4
    (5.0, 62, 100), # Bb
    (5.0, 66, 100), # D
    (5.0, 69, 100), # F
    (5.0, 73, 100), # A
]
for time, note, velocity in piano_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Drums in Bars 2-4
for bar in range(2, 5):
    start_time = bar * 1.5
    # Kick on 1
    dr = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.25)
    drums.notes.append(dr)
    # Hihat on &1
    dr = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.25, end=start_time + 0.5)
    drums.notes.append(dr)
    # Snare on 2
    dr = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.5, end=start_time + 0.75)
    drums.notes.append(dr)
    # Hihat on &2
    dr = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.75, end=start_time + 1.0)
    drums.notes.append(dr)
    # Kick on 3
    dr = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.0, end=start_time + 1.25)
    drums.notes.append(dr)
    # Hihat on &3
    dr = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.25, end=start_time + 1.5)
    drums.notes.append(dr)
    # Snare on 4
    dr = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.5, end=start_time + 1.75)
    drums.notes.append(dr)
    # Hihat on &4
    dr = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.75, end=start_time + 2.0)
    drums.notes.append(dr)

# Saxophone (Dante) - Motif (Bar 2, start at 1.5s)
# C7 - E7 - D7 - C7
sax_notes = [
    (1.5, 72, 100), # C7
    (1.75, 76, 100), # E7
    (2.0, 74, 100), # D7
    (2.25, 72, 100), # C7
    (3.0, 72, 100), # C7
    (3.25, 76, 100), # E7
    (3.5, 74, 100), # D7
    (3.75, 72, 100), # C7
]
for time, note, velocity in sax_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
