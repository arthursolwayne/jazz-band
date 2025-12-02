
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

# Bass line - walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5), (63, 1.875), (60, 2.25), (59, 2.625), # Dm7
    (62, 3.0), (63, 3.375), (60, 3.75), (59, 4.125), # Dm7
    (62, 4.5), (63, 4.875), (60, 5.25), (59, 5.625)  # Dm7
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano - 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2 - Dm7: D, F, A, C
    (62, 1.5), (64, 1.5), (67, 1.5), (69, 1.5),
    # Bar 3 - Gm7: G, Bb, D, F
    (67, 3.0), (69, 3.0), (71, 3.0), (64, 3.0),
    # Bar 4 - Dm7: D, F, A, C
    (62, 4.5), (64, 4.5), (67, 4.5), (69, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.5))

# Sax - melody: whisper at first, then a cry
# Bar 2: D - F - A - Bb (whisper)
# Bar 3: D - F - G - A (build tension)
# Bar 4: D - Bb - A - G (cry, resolution)
sax_notes = [
    (62, 1.5), (64, 1.875), (67, 2.25), (70, 2.625),  # Bar 2
    (62, 3.0), (64, 3.375), (66, 3.75), (67, 4.125),  # Bar 3
    (62, 4.5), (70, 4.875), (67, 5.25), (66, 5.625)   # Bar 4
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_cellar_intro.mid")
