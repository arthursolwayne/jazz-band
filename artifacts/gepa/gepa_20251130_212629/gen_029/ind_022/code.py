
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (42, 0.0, 0.125),
    (38, 0.375, 0.375), (42, 0.375, 0.125),
    (36, 0.75, 0.375), (42, 0.75, 0.125),
    (38, 1.125, 0.375), (42, 1.125, 0.125)
]
for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in D, chromatic approach
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375),  # D -> Eb
    (64, 2.25, 0.375), (65, 2.625, 0.375)   # E -> F
]
for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 1.875, 0.375), (67, 1.875, 0.375), # D7
    (62, 2.625, 0.375), (67, 2.625, 0.375)  # D7
]
for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Sax: Melody - short motif with space
sax_notes = [
    (62, 1.5, 0.25),     # D
    (64, 1.75, 0.25),    # E
    (62, 2.0, 0.25),     # D
    (64, 2.25, 0.25),    # E
    (62, 2.5, 0.25),     # D
    (64, 2.75, 0.25)     # E
]
for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes = [
    (65, 3.0, 0.375), (64, 3.375, 0.375),  # F -> E
    (62, 3.75, 0.375), (63, 4.125, 0.375)   # D -> Eb
]
for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 3.375, 0.375), (67, 3.375, 0.375), # D7
    (62, 4.125, 0.375), (67, 4.125, 0.375)  # D7
]
for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Sax: Melody - continuation of motif with space
sax_notes = [
    (62, 3.0, 0.25),     # D
    (64, 3.25, 0.25),    # E
    (62, 3.5, 0.25),     # D
    (64, 3.75, 0.25),    # E
    (62, 4.0, 0.25),     # D
    (64, 4.25, 0.25),    # E
    (62, 4.5, 0.25)      # D
]
for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375), (42, 3.0, 0.125),
    (38, 3.375, 0.375), (42, 3.375, 0.125),
    (36, 3.75, 0.375), (42, 3.75, 0.125),
    (38, 4.125, 0.375), (42, 4.125, 0.125)
]
for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line
bass_notes = [
    (63, 4.5, 0.375), (62, 4.875, 0.375),  # Eb -> D
    (64, 5.25, 0.375), (65, 5.625, 0.375)   # E -> F
]
for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 4.875, 0.375), (67, 4.875, 0.375), # D7
    (62, 5.625, 0.375), (67, 5.625, 0.375)  # D7
]
for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Sax: Melody - end with a question, not a statement
sax_notes = [
    (62, 4.5, 0.25),     # D
    (64, 4.75, 0.25),    # E
    (62, 5.0, 0.25),     # D
    (64, 5.25, 0.25),    # E
    (62, 5.5, 0.25),     # D
    (64, 5.75, 0.25)     # E
]
for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (42, 4.5, 0.125),
    (38, 4.875, 0.375), (42, 4.875, 0.125),
    (36, 5.25, 0.375), (42, 5.25, 0.125),
    (38, 5.625, 0.375), (42, 5.625, 0.125)
]
for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
