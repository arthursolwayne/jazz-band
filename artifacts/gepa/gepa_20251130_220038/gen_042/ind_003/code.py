
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
    (36, 0.0), (38, 0.375), (42, 0.375),  # bar 1
    (36, 0.75), (38, 1.125), (42, 1.125), (42, 1.5)  # bar 1 end
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    (62, 1.5), (64, 1.875), (63, 2.25), (65, 2.625),  # bar 2
    (67, 3.0), (69, 3.375), (68, 3.75), (70, 4.125),  # bar 3
    (72, 4.5), (74, 4.875), (73, 5.25), (75, 5.625)   # bar 4
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    (64, 2.0), (67, 2.0), (69, 2.0), (71, 2.0),  # D7 on beat 2 (bar 2)
    (67, 3.5), (70, 3.5), (72, 3.5), (74, 3.5),  # G7 on beat 2 (bar 3)
    (69, 5.0), (72, 5.0), (74, 5.0), (76, 5.0)   # Bm7 on beat 2 (bar 4)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax (Dante) - one short motif, make it sing
sax_notes = [
    (62, 1.5), (64, 1.75), (62, 2.0), (64, 2.5),  # bar 2
    (65, 3.0), (62, 3.5), (64, 4.0), (67, 4.5),  # bar 3
    (65, 5.0), (62, 5.5), (64, 6.0)              # bar 4
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
