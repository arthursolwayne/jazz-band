
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
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875), (36, 1.5, 0.375),
    (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif
sax_notes = [
    (60, 1.5, 0.375), (62, 1.875, 0.375), (63, 2.25, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Marcus - walking bass line in Fm
bass_notes = [
    (45, 1.5, 0.375), (46, 1.875, 0.375), (44, 2.25, 0.375), (42, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Diane - piano comping on 2 and 4
piano_notes = [
    (64, 1.875, 0.375), (67, 1.875, 0.375), (60, 1.875, 0.375),  # F7 on 2
    (64, 2.625, 0.375), (67, 2.625, 0.375), (60, 2.625, 0.375)   # F7 on 4
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone motif (reprise)
sax_notes = [
    (60, 3.0, 0.375), (62, 3.375, 0.375), (63, 3.75, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Marcus - walking bass line in Fm
bass_notes = [
    (45, 3.0, 0.375), (46, 3.375, 0.375), (44, 3.75, 0.375), (42, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Diane - piano comping on 2 and 4
piano_notes = [
    (64, 3.375, 0.375), (67, 3.375, 0.375), (60, 3.375, 0.375),  # F7 on 2
    (64, 4.125, 0.375), (67, 4.125, 0.375), (60, 4.125, 0.375)   # F7 on 4
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums in Bar 3
drum_notes = [
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (42, 3.1875, 0.1875), (42, 3.375, 0.1875), (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875), (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875), (42, 4.5, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone motif (completion)
sax_notes = [
    (64, 4.5, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Marcus - walking bass line in Fm
bass_notes = [
    (45, 4.5, 0.375), (46, 4.875, 0.375), (44, 5.25, 0.375), (42, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Diane - piano comping on 2 and 4
piano_notes = [
    (64, 4.875, 0.375), (67, 4.875, 0.375), (60, 4.875, 0.375),  # F7 on 2
    (64, 5.625, 0.375), (67, 5.625, 0.375), (60, 5.625, 0.375)   # F7 on 4
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums in Bar 4
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875), (42, 6.0, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
