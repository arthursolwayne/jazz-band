
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
    (36, 0.0), (38, 0.375), (42, 0.375),  # 1
    (36, 0.75), (38, 1.125), (42, 1.125),  # 2
    (36, 1.5), (38, 1.875), (42, 1.875),  # 3
    (36, 2.25), (38, 2.625), (42, 2.625)   # 4
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5), (41, 1.75), (38, 2.0), (40, 2.25),  # Bar 2
    (43, 2.5), (41, 2.75), (43, 3.0), (40, 3.25),  # Bar 3
    (38, 3.5), (41, 3.75), (38, 4.0), (40, 4.25),  # Bar 4
    (43, 4.5), (41, 4.75), (43, 5.0), (40, 5.25)   # Bar 4
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano.add_note(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))
piano.add_note(pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75))
piano.add_note(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75))
piano.add_note(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75))

# Bar 3: Bb7 (Bb-D-F-A)
piano.add_note(pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=2.75))
piano.add_note(pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75))
piano.add_note(pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75))
piano.add_note(pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75))

# Bar 4: Gm7 (G-Bb-D-F)
piano.add_note(pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75))
piano.add_note(pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75))
piano.add_note(pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75))
piano.add_note(pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=3.75))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Dm melody (D-F-A-D)
sax.add_note(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))
sax.add_note(pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0))
sax.add_note(pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25))

# Bar 3: Rest, leave it hanging
# Bar 4: Return and finish the motif (D-F-A-D)
sax.add_note(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75))
sax.add_note(pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0))
sax.add_note(pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25))
sax.add_note(pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
