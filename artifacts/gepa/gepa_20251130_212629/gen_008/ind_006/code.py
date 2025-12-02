
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
    (36, 0.0), (38, 0.375), (42, 0.1875),
    (36, 0.75), (38, 1.125), (42, 0.9375),
    (36, 1.5), (38, 1.875), (42, 1.6875),
    (36, 2.25), (38, 2.625), (42, 2.4375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    (36, 1.5), (37, 1.875), (35, 2.25), (34, 2.625),
    (36, 3.0), (37, 3.375), (35, 3.75), (34, 4.125),
    (36, 4.5), (37, 4.875), (35, 5.25), (34, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (43, 1.875), (47, 1.875), (49, 1.875), (51, 1.875),
    # Bar 3
    (43, 3.375), (47, 3.375), (49, 3.375), (51, 3.375),
    # Bar 4
    (43, 4.875), (47, 4.875), (49, 4.875), (51, 4.875)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Fm7 -> Bb -> Ab -> F
sax_notes = [
    (48, 1.5), # F
    (45, 1.875), # Bb
    (46, 2.25), # Ab
    (48, 2.625), # F
    (48, 3.0), # F
    (45, 3.375), # Bb
    (46, 3.75), # Ab
    (48, 4.125), # F
    (48, 4.5), # F
    (45, 4.875), # Bb
    (46, 5.25), # Ab
    (48, 5.625) # F
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
