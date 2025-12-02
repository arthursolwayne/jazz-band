
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))  # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))    # Hi-hat on every 8th

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in F
bass_notes = [
    (1.5, 45),  # F3
    (1.875, 47), # G3
    (2.25, 46),  # F#3
    (2.625, 45), # F3
    (2.625, 47), # G3
    (3.0, 49),   # A3
    (3.375, 48), # G#3
    (3.75, 47),  # G3
    (3.75, 49),  # A3
    (4.125, 50), # Bb3
    (4.5, 49),   # A3
    (4.875, 48), # G#3
    (5.25, 47),  # G3
    (5.625, 45), # F3
    (6.0, 45)    # F3
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Diane - 7th chords, comp on 2 and 4
piano_notes = [
    (1.875, 64),  # C4
    (1.875, 69),  # G4
    (1.875, 67),  # F#4
    (1.875, 65),  # E4
    (3.0, 64),    # C4
    (3.0, 69),    # G4
    (3.0, 67),    # F#4
    (3.0, 65),    # E4
    (4.5, 64),    # C4
    (4.5, 71),    # A4
    (4.5, 69),    # G4
    (4.5, 67),    # F#4
    (4.5, 65),    # E4
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for bar in range(2, 5):
    start = (bar - 2) * 1.5
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))  # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))  # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))  # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))  # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5))  # Hi-hat on every 8th

# Dante - Tenor sax melody (bars 2-4)
# Whisper at first, then a cry
sax_notes = [
    (1.5, 62),  # E4 (quiet, low)
    (1.625, 62), # E4
    (1.75, 64),  # F4
    (1.875, 62), # E4
    (2.0, 66),   # A4 (rise)
    (2.125, 67), # A#4
    (2.25, 69),  # C5
    (2.375, 67), # A#4
    (2.5, 69),   # C5
    (2.625, 64), # F4
    (2.75, 62),  # E4
    (2.875, 60), # D4
    (3.0, 62),   # E4
    (3.125, 64), # F4
    (3.25, 62),  # E4
    (3.375, 60), # D4
    (3.5, 62),   # E4
    (3.625, 64), # F4
    (3.75, 66),  # A4
    (3.875, 67), # A#4
    (4.0, 69),   # C5
    (4.125, 67), # A#4
    (4.25, 69),  # C5
    (4.375, 64), # F4
    (4.5, 62),   # E4
    (4.625, 60), # D4
    (4.75, 62),  # E4
    (4.875, 64), # F4
    (5.0, 62),   # E4
    (5.125, 60), # D4
    (5.25, 62),  # E4
    (5.375, 64), # F4
    (5.5, 66),   # A4
    (5.625, 67), # A#4
    (5.75, 69),  # C5
    (5.875, 67), # A#4
    (6.0, 69)    # C5 (end on a cry)
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_moment.mid')
