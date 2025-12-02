
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
    (36, 0.0), (38, 0.375), (42, 0.375), (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, Fm7 bass line
bass_notes = [
    (64, 1.5), (65, 1.75), (63, 2.0), (62, 2.25),  # Fm7
    (64, 2.5), (65, 2.75), (63, 3.0), (62, 3.25),  # Fm7
    (64, 3.5), (65, 3.75), (63, 4.0), (62, 4.25),  # Fm7
    (64, 4.5), (65, 4.75), (63, 5.0), (62, 5.25)   # Fm7
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (2 and 4)
    (64, 2.0), (67, 2.0), (69, 2.0), (71, 2.0),
    (64, 2.5), (67, 2.5), (69, 2.5), (71, 2.5),
    # Bar 3: Fm7 (2 and 4)
    (64, 3.0), (67, 3.0), (69, 3.0), (71, 3.0),
    (64, 3.5), (67, 3.5), (69, 3.5), (71, 3.5),
    # Bar 4: Fm7 (2 and 4)
    (64, 4.0), (67, 4.0), (69, 4.0), (71, 4.0),
    (64, 4.5), (67, 4.5), (69, 4.5), (71, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes.extend([
    (36, 1.5), (38, 1.875), (42, 1.875), (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375), (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875), (36, 5.25), (38, 5.625), (42, 5.625)
])
for note, time in drum_notes[9:]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor sax, one short motif, make it sing
# Motif: F - Ab - Bb - D (Fm7 arpeggio) on beat 1, then leave it hanging
sax_notes = [
    (64, 1.5), (66, 1.875), (67, 2.25), (71, 2.625),  # Start the motif
    (64, 3.0), (66, 3.375), (67, 3.75), (71, 4.125),  # Repeat it
    (64, 4.5), (66, 4.875), (67, 5.25), (71, 5.625)   # Finish it
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
