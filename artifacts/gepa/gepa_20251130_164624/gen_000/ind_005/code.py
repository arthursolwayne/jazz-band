
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (61, 2.25, 0.375), (60, 2.625, 0.375),
    (62, 3.0, 0.375), (63, 3.375, 0.375), (61, 3.75, 0.375), (60, 4.125, 0.375),
    (62, 4.5, 0.375), (63, 4.875, 0.375), (61, 5.25, 0.375), (60, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano - 7th chords on 2 and 4, comping in Dm7
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    (62, 1.5, 0.1875), (64, 1.5, 0.1875), (67, 1.5, 0.1875), (69, 1.5, 0.1875),
    # Bar 3: Dm7 (D F A C)
    (62, 3.0, 0.1875), (64, 3.0, 0.1875), (67, 3.0, 0.1875), (69, 3.0, 0.1875),
    # Bar 4: Dm7 (D F A C)
    (62, 4.5, 0.1875), (64, 4.5, 0.1875), (67, 4.5, 0.1875), (69, 4.5, 0.1875),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Saxophone - Motif: D (62), F (64), Eb (63), D (62) - short, sing, leave it hanging
sax_notes = [
    (62, 1.5, 0.25), (64, 1.75, 0.25), (63, 2.0, 0.25), (62, 2.25, 0.25),
    (62, 2.5, 0.25), (64, 2.75, 0.25), (63, 3.0, 0.25), (62, 3.25, 0.25),
    (62, 3.5, 0.25), (64, 3.75, 0.25), (63, 4.0, 0.25), (62, 4.25, 0.25)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums continue through bars 2-4
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
