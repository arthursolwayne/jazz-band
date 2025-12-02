
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
    (36, 1.125), (38, 1.5), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, D minor
bass_notes = [
    (62, 1.5), (63, 1.75), (64, 2.0), (62, 2.25),  # Dm7
    (62, 2.5), (63, 2.75), (64, 3.0), (62, 3.25),  # Dm7
    (62, 3.5), (63, 3.75), (64, 4.0), (62, 4.25),  # Dm7
    (62, 4.5), (63, 4.75), (64, 5.0), (62, 5.25)   # Dm7
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7
    (62, 2.0), (67, 2.0), (72, 2.0), (74, 2.0),
    # Bar 3: Dm7
    (62, 3.0), (67, 3.0), (72, 3.0), (74, 3.0),
    # Bar 4: Dm7
    (62, 4.0), (67, 4.0), (72, 4.0), (74, 4.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D - F - G - Bb (Dm7) -> G - Bb - D - F (G7) -> D - F - G - Bb (Dm7)
sax_notes = [
    # Bar 2: D - F - G - Bb
    (62, 1.5), (64, 1.75), (67, 2.0), (69, 2.25),
    # Bar 3: G - Bb - D - F
    (67, 2.5), (69, 2.75), (62, 3.0), (64, 3.25),
    # Bar 4: D - F - G - Bb
    (62, 3.5), (64, 3.75), (67, 4.0), (69, 4.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.625), (38, 3.0), (42, 3.0),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.875), (38, 5.25), (42, 5.25)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('jazz_intro.mid')
