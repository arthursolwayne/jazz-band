
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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

# Bass: Walking line, chromatic approaches, no repeated notes
# C7 -> B -> C -> D -> C
bass_notes = [
    (60, 1.5, 1.75), (61, 1.75, 2.0), (60, 2.0, 2.25), (62, 2.25, 2.5),
    (60, 2.5, 2.75), (61, 2.75, 3.0), (60, 3.0, 3.25), (62, 3.25, 3.5),
    (60, 3.5, 3.75), (61, 3.75, 4.0), (60, 4.0, 4.25), (62, 4.25, 4.5),
    (60, 4.5, 4.75), (61, 4.75, 5.0), (60, 5.0, 5.25), (62, 5.25, 5.5)
]
for note, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
# C7 on 2, F7 on 4
piano_notes = [
    # Bar 2: C7 on beat 2
    (60, 2.0, 2.25), (64, 2.0, 2.25), (67, 2.0, 2.25),
    # Bar 3: F7 on beat 4
    (65, 4.0, 4.25), (69, 4.0, 4.25), (72, 4.0, 4.25),
    # Bar 4: C7 on beat 2
    (60, 5.0, 5.25), (64, 5.0, 5.25), (67, 5.0, 5.25)
]
for note, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Sax: Melody - one short motif, make it sing
# C - D - B - C
sax_notes = [
    (60, 1.5, 1.75), (62, 1.75, 2.0), (61, 2.0, 2.25), (60, 2.25, 2.5),
    (60, 3.5, 3.75), (62, 3.75, 4.0), (61, 4.0, 4.25), (60, 4.25, 4.5),
    (60, 5.5, 5.75), (62, 5.75, 6.0), (61, 6.0, 6.25), (60, 6.25, 6.5)
]
for note, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Drums: continue for bars 2-4
drum_notes = [
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_intro.mid")
