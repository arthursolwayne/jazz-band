
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in Dm
bass_notes = [
    (62, 1.5), (60, 1.875), (62, 2.25), (64, 2.625),
    (62, 3.0), (60, 3.375), (62, 3.75), (64, 4.125),
    (62, 4.5), (60, 4.875), (62, 5.25), (64, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Diane - Piano comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (64, 1.875), (67, 1.875), (69, 1.875), (71, 1.875),
    (64, 3.0), (67, 3.0), (69, 3.0), (71, 3.0),
    
    # Bar 3 (3.0 - 4.5s)
    (64, 3.375), (67, 3.375), (69, 3.375), (71, 3.375),
    (64, 4.5), (67, 4.5), (69, 4.5), (71, 4.5),
    
    # Bar 4 (4.5 - 6.0s)
    (64, 4.875), (67, 4.875), (69, 4.875), (71, 4.875),
    (64, 6.0), (67, 6.0), (69, 6.0), (71, 6.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.125))

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante - Tenor sax melody in Dm
sax_notes = [
    (62, 1.5), (64, 1.875), (62, 2.25), (60, 2.625),
    (62, 3.0), (64, 3.375), (62, 3.75), (60, 4.125),
    (62, 4.5), (64, 4.875), (62, 5.25), (60, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
