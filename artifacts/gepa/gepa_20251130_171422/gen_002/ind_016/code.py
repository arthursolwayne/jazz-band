
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.375),
    (42, 0.75), (42, 1.125), (36, 1.5), (38, 1.875),
    (42, 1.5), (42, 1.875), (42, 2.25), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line, chromatic approaches, no same note twice
bass_notes = [
    (62, 1.5), (63, 1.875), (60, 2.25), (61, 2.625),
    (62, 3.0), (63, 3.375), (60, 3.75), (61, 4.125),
    (62, 4.5), (63, 4.875), (60, 5.25), (61, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: Diane, 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2: Dm7
    (62, 2.625), (67, 2.625), (69, 2.625), (71, 2.625),
    # Bar 3, beat 2: G7
    (67, 4.125), (72, 4.125), (74, 4.125), (76, 4.125),
    # Bar 4, beat 2: Cm7
    (60, 5.625), (65, 5.625), (67, 5.625), (69, 5.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.875),
    (42, 2.25), (42, 2.625), (36, 3.0), (38, 3.375),
    (42, 3.0), (42, 3.375), (42, 3.75), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.875),
    (42, 5.25), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Dante, melody - one short motif, make it sing, leave it hanging
sax_notes = [
    (62, 1.5), (65, 1.875), (62, 2.25), (67, 2.625),
    (65, 3.0), (62, 3.375), (67, 3.75), (65, 4.125),
    (62, 4.5), (65, 4.875), (67, 5.25), (65, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
