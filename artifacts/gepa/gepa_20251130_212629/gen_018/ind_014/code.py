
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (42, 0.5), (42, 0.625), (42, 0.75), (42, 0.875), (36, 1.125), (38, 1.5),
    (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line, chromatic approaches, Dm7: D F A C
bass_notes = [
    (62, 1.5), (61, 1.75), (63, 2.0), (60, 2.25),
    (62, 2.5), (61, 2.75), (63, 3.0), (60, 3.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
# Dm7 on 2, G7 on 4
piano_notes = [
    (62, 2.0), (64, 2.0), (67, 2.0), (69, 2.0),  # Dm7
    (67, 3.0), (71, 3.0), (74, 3.0), (76, 3.0)   # G7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Dante: Motif with rhythmic tension, start it, leave it hanging
sax_notes = [
    (67, 1.5, 0.4),  # D (Dm7)
    (69, 1.9, 0.2),  # F (chromatic approach)
    (67, 2.1, 0.2),  # D (back to D)
    (69, 2.3, 0.2),  # F
    (67, 2.5, 0.2),  # D
    (71, 2.7, 0.2),  # G (leading tone)
    (67, 2.9, 0.1),  # D (end on a rest)
]
for note, time, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line, chromatic approaches
bass_notes = [
    (62, 3.0), (61, 3.25), (63, 3.5), (60, 3.75),
    (62, 4.0), (61, 4.25), (63, 4.5), (60, 4.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
# Dm7 on 2, G7 on 4
piano_notes = [
    (62, 3.5), (64, 3.5), (67, 3.5), (69, 3.5),  # Dm7
    (67, 4.5), (71, 4.5), (74, 4.5), (76, 4.5)   # G7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.0), (42, 3.125), (42, 3.25), (42, 3.375),
    (42, 3.5), (42, 3.625), (42, 3.75), (42, 3.875), (36, 4.125), (38, 4.5),
    (42, 4.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line, chromatic approaches
bass_notes = [
    (62, 4.5), (61, 4.75), (63, 5.0), (60, 5.25),
    (62, 5.5), (61, 5.75), (63, 6.0), (60, 6.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
# Dm7 on 2, G7 on 4
piano_notes = [
    (62, 5.0), (64, 5.0), (67, 5.0), (69, 5.0),  # Dm7
    (67, 6.0), (71, 6.0), (74, 6.0), (76, 6.0)   # G7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.625), (42, 4.75), (42, 4.875),
    (42, 5.0), (42, 5.125), (42, 5.25), (42, 5.375), (36, 5.625), (38, 6.0),
    (42, 6.0)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Finish the motif with a question, leave it hanging
sax_notes = [
    (67, 4.5, 0.4),  # D (Dm7)
    (69, 4.9, 0.2),  # F (chromatic approach)
    (67, 5.1, 0.2),  # D (back to D)
    (69, 5.3, 0.2),  # F
    (67, 5.5, 0.2),  # D
    (71, 5.7, 0.2),  # G (leading tone)
    (67, 5.9, 0.1)   # D (end on a rest)
]
for note, time, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
