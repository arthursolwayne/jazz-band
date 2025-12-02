
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line (F2-G2, MIDI 53-55), roots and fifths with chromatic approaches
bass_notes = [
    (53, 1.5), (54, 1.875), (55, 2.25), (53, 2.625),
    (53, 3.0), (54, 3.375), (55, 3.75), (53, 4.125),
    (53, 4.5), (54, 4.875), (55, 5.25), (53, 5.625)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (64, 1.5), (72, 1.5), (76, 1.5), (78, 1.5),
    (64, 1.5), (67, 1.5), (72, 1.5), (76, 1.5)
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(n)

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    (67, 3.0), (74, 3.0), (76, 3.0), (72, 3.0),
    (67, 3.0), (69, 3.0), (74, 3.0), (76, 3.0)
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(n)

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    (72, 4.5), (76, 4.5), (79, 4.5), (74, 4.5),
    (72, 4.5), (76, 4.5), (79, 4.5), (74, 4.5)
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(n)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it
# Motif: F (64) - Ab (67) - D (72), played on beat 1 of bar 2 and 3.5 of bar 4

sax_notes = [
    (64, 1.5), (67, 1.875), (72, 2.25),
    (64, 3.5), (67, 3.875), (72, 4.25)
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Fill the bar with drums
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
