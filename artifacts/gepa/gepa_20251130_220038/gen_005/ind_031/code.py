
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
    (36, 0.75), (38, 1.125), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (62, 1.5), (63, 1.75), (60, 2.0), (62, 2.25),
    (64, 2.5), (65, 2.75), (62, 3.0), (64, 3.25),
    (65, 3.5), (67, 3.75), (64, 4.0), (67, 4.25),
    (69, 4.5), (70, 4.75), (67, 5.0), (69, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (60, 1.75), (64, 1.75), (67, 1.75), (71, 1.75), # Dm7 on beat 2
    (62, 2.75), (65, 2.75), (69, 2.75), (72, 2.75), # F7 on beat 4
    (62, 3.75), (65, 3.75), (69, 3.75), (72, 3.75), # F7 on beat 4
    (64, 4.75), (67, 4.75), (71, 4.75), (74, 4.75)  # Bb7 on beat 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.25), (42, 2.375), (42, 2.5), (42, 2.625),
    (36, 2.75), (38, 3.125), (42, 2.75), (42, 2.875), (42, 3.0), (42, 3.125),
    (36, 3.5), (38, 3.875), (42, 3.5), (42, 3.625), (42, 3.75), (42, 3.875),
    (36, 4.25), (38, 4.625), (42, 4.25), (42, 4.375), (42, 4.5), (42, 4.625),
    (36, 5.0), (38, 5.375), (42, 5.0), (42, 5.125), (42, 5.25), (42, 5.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5), (65, 1.75), (67, 2.0), (65, 2.25),
    (62, 2.5), (65, 2.75), (67, 3.0), (65, 3.25),
    (62, 3.5), (65, 3.75), (67, 4.0), (65, 4.25),
    (62, 4.5), (65, 4.75), (67, 5.0), (65, 5.25),
    (62, 5.5), (65, 5.75), (67, 6.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("waynes_moment.mid")
