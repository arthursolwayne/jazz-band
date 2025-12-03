
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.375),
    (42, 0.75), (42, 1.125), (36, 1.5), (38, 1.875),
    (42, 1.5), (42, 1.875), (42, 2.25), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5), (40, 1.875), (38, 2.25), (41, 2.625),
    (43, 2.75), (42, 3.125), (40, 3.5), (43, 3.875),
    (42, 4.25), (44, 4.625), (43, 5.0), (41, 5.375)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    (62, 1.5), (67, 1.5), (69, 1.5), (64, 1.5),
    # Bar 3: Gm7 (G Bb D F)
    (67, 2.75), (71, 2.75), (69, 2.75), (65, 2.75),
    # Bar 4: A7 (A C# E G)
    (70, 4.0), (75, 4.0), (77, 4.0), (71, 4.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F# (67), A (69), then rest on the last eighth of bar 2
sax_notes = [
    (62, 1.5), (67, 1.875), (69, 2.25), (69, 2.625),
    (62, 3.5), (67, 3.875), (69, 4.25), (69, 4.625),
    (62, 5.0), (67, 5.375), (69, 5.75), (69, 6.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
