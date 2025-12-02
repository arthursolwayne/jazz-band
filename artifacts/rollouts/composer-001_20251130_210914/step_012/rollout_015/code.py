
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875), (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875), (42, 0.5625, 0.1875), (36, 0.75, 0.375), (38, 1.125, 0.375),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875), (42, 1.3125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line in D, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (60, 2.25, 0.375), (62, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 2
    (67, 1.875, 0.1875), (69, 1.875, 0.1875), (72, 1.875, 0.1875), (71, 1.875, 0.1875),
    # Bar 3: D7 on beat 4
    (67, 3.0, 0.1875), (69, 3.0, 0.1875), (72, 3.0, 0.1875), (71, 3.0, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax - motif in D, start on beat 1
# Motif: D - E - F# - D (melodic minor)
sax_notes = [
    (62, 1.5, 0.375), (64, 1.875, 0.375), (66, 2.25, 0.375), (62, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line in D, chromatic approaches
bass_notes = [
    (64, 3.0, 0.375), (65, 3.375, 0.375), (62, 3.75, 0.375), (64, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: D7 on beat 2
    (67, 3.375, 0.1875), (69, 3.375, 0.1875), (72, 3.375, 0.1875), (71, 3.375, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax - repeat motif, but end on beat 3
sax_notes = [
    (62, 3.0, 0.375), (64, 3.375, 0.375), (66, 3.75, 0.375), (62, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line in D, chromatic approaches
bass_notes = [
    (65, 4.5, 0.375), (67, 4.875, 0.375), (64, 5.25, 0.375), (65, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: D7 on beat 2
    (67, 4.875, 0.1875), (69, 4.875, 0.1875), (72, 4.875, 0.1875), (71, 4.875, 0.1875),
    # Bar 4: D7 on beat 4
    (67, 6.0, 0.1875), (69, 6.0, 0.1875), (72, 6.0, 0.1875), (71, 6.0, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax - complete the motif, end on beat 4
sax_notes = [
    (62, 4.5, 0.375), (64, 4.875, 0.375), (66, 5.25, 0.375), (62, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Drums: Bar 4
drum_notes = [
    # Bar 4
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875), (42, 4.6875, 0.1875),
    (42, 4.875, 0.1875), (42, 5.0625, 0.1875), (36, 5.25, 0.375), (38, 5.625, 0.375),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875), (42, 5.8125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
