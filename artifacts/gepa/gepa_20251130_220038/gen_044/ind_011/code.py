
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (42, 0.5), (42, 0.625), (42, 0.75), (42, 0.875), (36, 1.125), (38, 1.5),
    (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875), (42, 2.0), (42, 2.125),
    (42, 2.25), (42, 2.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Dm
bass_notes = [
    (62, 1.5), (64, 1.875), (60, 2.25), (62, 2.625),
    (64, 3.0), (67, 3.375), (64, 3.75), (62, 4.125),
    (60, 4.5), (62, 4.875), (64, 5.25), (67, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on beat 2
    (62, 2.0), (67, 2.0), (64, 2.0), (69, 2.0),
    # Bar 3: Gm7 on beat 2
    (67, 3.0), (72, 3.0), (69, 3.0), (74, 3.0),
    # Bar 4: Cm7 on beat 2
    (60, 4.0), (65, 4.0), (62, 4.0), (67, 4.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar2 = [
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875),
    (42, 2.0), (42, 2.125), (42, 2.25), (42, 2.375), (36, 2.625), (38, 3.0),
    (42, 3.0), (42, 3.125), (42, 3.25), (42, 3.375), (42, 3.5), (42, 3.625),
    (42, 3.75), (42, 3.875), (36, 4.125), (38, 4.5), (42, 4.5), (42, 4.625),
    (42, 4.75), (42, 4.875), (42, 5.0), (42, 5.125), (42, 5.25), (42, 5.375)
]
for note, time in drum_notes_bar2:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor sax melody, one short motif, make it sing
# Start it, leave it hanging. Come back and finish it. No scale runs.
sax_notes = [
    # Bar 2: Start the motif
    (62, 1.5), (65, 1.875), (67, 2.25), (69, 2.625),
    # Bar 3: Leave it hanging
    (67, 3.0), (65, 3.375),
    # Bar 4: Come back and finish it
    (62, 4.5), (65, 4.875), (67, 5.25), (69, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
