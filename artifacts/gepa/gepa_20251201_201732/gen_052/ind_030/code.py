
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Drums - Bar 1
drum_notes = [
    (0.0, 36, 100),   # Kick on 1
    (0.375, 42, 80),  # Hihat on 2
    (0.75, 38, 100),  # Snare on 3
    (1.125, 42, 80),  # Hihat on 4
    (1.375, 36, 90),  # Kick on 4 (slightly late, syncopated)
]

for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.0625)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass - Bar 2 (walking line with chromatic approaches)
bass_notes = [
    (1.5, 38, 70),   # D2
    (1.875, 40, 70), # Eb2
    (2.25, 43, 70),  # G2
    (2.625, 42, 70), # F#2 (chromatic approach)
    # Bar 3
    (3.0, 38, 70),   # D2
    (3.375, 41, 70), # E2
    (3.75, 43, 70),  # G2
    (4.125, 42, 70), # F#2
    # Bar 4
    (4.5, 38, 70),   # D2
    (4.875, 40, 70), # Eb2
    (5.25, 43, 70),  # G2
    (5.625, 42, 70), # F#2
]

for time, note, velocity in bass_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano - Bar 2: Open voicing, C7 (C E G B D)
piano_notes = [
    (1.5, 72, 100),  # C5
    (1.5, 67, 80),   # E4
    (1.5, 60, 80),   # G3
    (1.5, 57, 60),   # B2
    (1.5, 62, 60),   # D3
    # Bar 3: F7 (F A C E G)
    (3.0, 76, 100),  # F5
    (3.0, 71, 80),   # A4
    (3.0, 65, 80),   # C4
    (3.0, 62, 60),   # E3
    (3.0, 67, 60),   # G3
    # Bar 4: G7 (G B D F# A)
    (4.5, 78, 100),  # G5
    (4.5, 73, 80),   # B4
    (4.5, 67, 80),   # D4
    (4.5, 64, 60),   # F#3
    (4.5, 69, 60),   # A3
]
for time, note, velocity in piano_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Sax - Bar 2: Haunting motif, incomplete, "questioning" melody
sax_notes = [
    (1.5, 62, 80),   # D4
    (1.625, 66, 80), # F4
    (1.75, 62, 80),  # D4 (rest on beat 3)
    # Bar 3: Contrast, higher and more intense
    (3.0, 67, 100),  # E4
    (3.125, 71, 100), # A4
    (3.25, 67, 100), # E4 (rest on beat 3)
    # Bar 4: Return to motif, unfinished, haunting
    (4.5, 62, 80),   # D4
    (4.625, 66, 80), # F4
    (4.75, 62, 80),  # D4 (rest on beat 3)
]
for time, note, velocity in sax_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note_obj)

# Drums - Bars 2-4
drum_notes = [
    # Bar 2
    (1.5, 36, 100),   # Kick on 1
    (1.875, 38, 100), # Snare on 2
    (2.25, 36, 100),  # Kick on 3
    (2.625, 38, 100), # Snare on 4
    (2.875, 42, 100), # Hihat on 4 (syncopated)
    # Bar 3
    (3.0, 36, 100),   # Kick on 1
    (3.375, 38, 100), # Snare on 2
    (3.75, 36, 100),  # Kick on 3
    (4.125, 38, 100), # Snare on 4
    (4.375, 42, 100), # Hihat on 4
    # Bar 4
    (4.5, 36, 100),   # Kick on 1
    (4.875, 38, 100), # Snare on 2
    (5.25, 36, 100),  # Kick on 3
    (5.625, 38, 100), # Snare on 4
    (5.875, 42, 100), # Hihat on 4
]

for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.0625)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')
