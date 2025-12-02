
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
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.375),    # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.375),   # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (53, 1.5, 0.375),  # Fm7 - F
    (52, 1.875, 0.375), # Eb - chromatic
    (50, 2.25, 0.375),  # D - chromatic
    (48, 2.625, 0.375)  # C - chromatic
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (50, 1.875, 0.375),  # D7 - D
    (48, 1.875, 0.375),  # C
    (53, 1.875, 0.375),  # F
    (52, 1.875, 0.375),  # Eb
    (50, 2.625, 0.375),  # D7 - D
    (48, 2.625, 0.375),  # C
    (53, 2.625, 0.375),  # F
    (52, 2.625, 0.375)   # Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Melody - short motif, whisper then cry
sax_notes = [
    (53, 1.5, 0.125),    # F
    (50, 1.625, 0.125),  # D
    (48, 1.75, 0.125),   # C
    (53, 1.875, 0.125),  # F (end of bar 2)
    (53, 2.25, 0.125),   # F (start of bar 3, repeat motif)
    (50, 2.375, 0.125),  # D
    (48, 2.5, 0.125),    # C
    (60, 2.625, 0.125)   # G (cry)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approach
bass_notes = [
    (53, 3.0, 0.375),  # F
    (52, 3.375, 0.375), # Eb
    (50, 3.75, 0.375),  # D
    (48, 4.125, 0.375)  # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (50, 3.375, 0.375),  # D7 - D
    (48, 3.375, 0.375),  # C
    (53, 3.375, 0.375),  # F
    (52, 3.375, 0.375),  # Eb
    (50, 4.125, 0.375),  # D7 - D
    (48, 4.125, 0.375),  # C
    (53, 4.125, 0.375),  # F
    (52, 4.125, 0.375)   # Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Melody - continuation of motif
sax_notes = [
    (53, 3.0, 0.125),    # F
    (50, 3.125, 0.125),  # D
    (48, 3.25, 0.125),   # C
    (53, 3.375, 0.125),  # F
    (53, 3.75, 0.125),   # F
    (50, 3.875, 0.125),  # D
    (48, 4.0, 0.125),    # C
    (60, 4.125, 0.125)   # G (cry)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: continue pattern
drum_notes = [
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.375),    # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.375),  # Hihat on 2
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.375),   # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approach
bass_notes = [
    (53, 4.5, 0.375),  # F
    (52, 4.875, 0.375), # Eb
    (50, 5.25, 0.375),  # D
    (48, 5.625, 0.375)  # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (50, 4.875, 0.375),  # D7 - D
    (48, 4.875, 0.375),  # C
    (53, 4.875, 0.375),  # F
    (52, 4.875, 0.375),  # Eb
    (50, 5.625, 0.375),  # D7 - D
    (48, 5.625, 0.375),  # C
    (53, 5.625, 0.375),  # F
    (52, 5.625, 0.375)   # Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Melody - end with a resolution
sax_notes = [
    (53, 4.5, 0.125),    # F
    (50, 4.625, 0.125),  # D
    (48, 4.75, 0.125),   # C
    (53, 4.875, 0.125),  # F
    (53, 5.25, 0.125),   # F
    (50, 5.375, 0.125),  # D
    (48, 5.5, 0.125),    # C
    (53, 5.625, 0.125)   # F (resolution)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: continue pattern
drum_notes = [
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.375),    # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.375),   # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_intro.mid")
