
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
    (36, 2.25), (38, 2.625), (42, 2.625),
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F, chromatic approaches
bass_notes = [
    (53, 1.5), (55, 1.75), (53, 2.0), (52, 2.25),
    (53, 2.5), (55, 2.75), (53, 3.0), (52, 3.25),
    (53, 3.5), (55, 3.75), (53, 4.0), (52, 4.25),
    (53, 4.5), (55, 4.75), (53, 5.0), (52, 5.25),
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    (64, 2.0), (67, 2.0), (69, 2.0), (71, 2.0),
    # Bar 3: Bb7 on beat 2
    (71, 3.0), (74, 3.0), (76, 3.0), (78, 3.0),
    # Bar 4: E7 on beat 2
    (76, 4.0), (79, 4.0), (81, 4.0), (83, 4.0),
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Dante: Tenor sax motif - start it, leave it hanging, come back and finish
# Motif: F, G#, Bb, F (staccato on first note, legato on last)
sax_notes = [
    (64, 1.5, 0.25), (71, 1.75, 0.25), (67, 2.0, 0.25),  # Bar 2
    (64, 2.5, 0.25), (71, 2.75, 0.25), (67, 3.0, 0.25),  # Bar 3
    (64, 3.5, 0.25), (71, 3.75, 0.25), (67, 4.0, 0.25),  # Bar 4
    (64, 4.5, 0.25), (71, 4.75, 0.25), (67, 5.0, 0.25),  # Bar 4
]
for note, time, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.save('jazz_intro.mid')
