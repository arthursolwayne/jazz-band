
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
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    (62, 1.5), (65, 1.875), (64, 2.25), (62, 2.625),  # D - F - Eb - D
    (62, 3.0), (65, 3.375), (64, 3.75), (62, 4.125),  # D - F - Eb - D
    (62, 4.5), (65, 4.875), (64, 5.25), (62, 5.625)   # D - F - Eb - D
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F - A - D - F)
piano_notes = [
    (62, 1.5), (64, 1.5), (65, 1.5), (62, 1.5),  # D - F - A - D
    # Bar 3: Gm7 (Bb - D - G - Bb)
    (60, 3.0), (62, 3.0), (65, 3.0), (60, 3.0),  # G - Bb - D - G
    # Bar 4: Cm7 (Eb - G - C - Eb)
    (64, 4.5), (65, 4.5), (67, 4.5), (64, 4.5)   # C - Eb - G - C
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F - Eb - D (Dm7 arpeggio)
sax_notes = [
    (62, 1.5), (64, 1.5), (64, 1.875), (62, 2.25),
    (62, 4.5), (64, 4.5), (64, 4.875), (62, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dm_intro.mid")
