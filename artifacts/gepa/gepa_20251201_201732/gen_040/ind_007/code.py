
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    (78, 1.5), (82, 1.75), (80, 2.0), (77, 2.25),
    (80, 2.5), (84, 2.75), (82, 3.0), (79, 3.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [(77, 1.5), (82, 1.5), (84, 1.5), (87, 1.5)]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.5))

# Bar 3: Bbm7 (Bb, D, F, Ab)
piano_notes = [(70, 2.5), (74, 2.5), (77, 2.5), (79, 2.5)]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.5))

# Bar 4: E7 (E, G#, B, D)
piano_notes = [(76, 3.5), (81, 3.5), (84, 3.5), (79, 3.5)]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.5))

# Sax: One short motif, make it sing
# Start on F, then G, then F again, leave it hanging
sax_notes = [
    (77, 1.5), (78, 1.75), (77, 2.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Drums continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875), (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375), (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
