
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

# Bass line - walking line with chromatic approaches
bass_notes = [
    (35, 1.5), (36, 1.875), (34, 2.25), (35, 2.625),
    (36, 3.0), (37, 3.375), (35, 3.75), (36, 4.125),
    (37, 4.5), (38, 4.875), (36, 5.25), (37, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano - 7th chords on 2 and 4, comp on 2nd and 4th beats
# Fm7 = F, Ab, C, D
# Bb7 = Bb, D, F, Ab
# Cm7 = C, Eb, G, Bb
# Eb7 = Eb, G, Bb, D
piano_notes = [
    # Bar 2
    (53, 3.0), (60, 3.0), (64, 3.0), (65, 3.0),
    # Bar 3
    (56, 4.5), (63, 4.5), (67, 4.5), (69, 4.5),
    # Bar 4
    (60, 6.0), (65, 6.0), (68, 6.0), (71, 6.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax - short motif, starts on F, ends on Ab, with space in between
sax_notes = [
    (53, 1.5), (57, 1.75), (59, 2.0), (60, 2.25),  # Bar 2
    (60, 2.5), (62, 2.75), (64, 3.0), (65, 3.25),  # Bar 3
    (65, 3.5), (67, 3.75), (69, 4.0), (71, 4.25),  # Bar 4
    (71, 4.5), (69, 4.75), (67, 5.0), (65, 5.25)   # Bar 4
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.125))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
