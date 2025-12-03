
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
bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3
drum_notes = [
    (36, bar1_start + 0.0, 0.25),
    (36, bar1_start + 0.75, 0.25),
    (38, bar1_start + 0.25, 0.25),
    (38, bar1_start + 0.75, 0.25),
    (42, bar1_start + 0.0, 0.5),
    (42, bar1_start + 0.5, 0.5),
    (42, bar1_start + 1.0, 0.5),
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bass line (walking line, D2-G2, roots and fifths with chromatic approaches)
bass_notes = [
    # Bar 2 (Fm7): F, C, Eb, D
    (65, bar2_start + 0.0, 0.25),  # F2
    (67, bar2_start + 0.25, 0.25), # C3
    (64, bar2_start + 0.5, 0.25),  # Eb3 (chromatic approach)
    (62, bar2_start + 0.75, 0.25),  # D3

    # Bar 3 (Ab7): Ab, Eb, G, F
    (70, bar3_start + 0.0, 0.25),  # Ab2
    (72, bar3_start + 0.25, 0.25), # Eb3
    (71, bar3_start + 0.5, 0.25),  # G3 (chromatic approach)
    (69, bar3_start + 0.75, 0.25),  # F3

    # Bar 4 (Bbm7): Bb, F, Ab, G
    (71, bar4_start + 0.0, 0.25),  # Bb2
    (73, bar4_start + 0.25, 0.25), # F3
    (70, bar4_start + 0.5, 0.25),  # Ab3 (chromatic approach)
    (69, bar4_start + 0.75, 0.25),  # G3
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (65, bar2_start + 0.0, 0.25),  # F2
    (68, bar2_start + 0.0, 0.25),  # Ab2
    (67, bar2_start + 0.0, 0.25),  # C3
    (69, bar2_start + 0.0, 0.25),  # D3

    # Bar 3: Ab7 (Ab, C, Eb, F)
    (70, bar3_start + 0.0, 0.25),  # Ab2
    (72, bar3_start + 0.0, 0.25),  # C3
    (71, bar3_start + 0.0, 0.25),  # Eb3
    (71, bar3_start + 0.0, 0.25),  # F3 (resolve)

    # Bar 4: Bbm7 (Bb, D, F, G)
    (71, bar4_start + 0.0, 0.25),  # Bb2
    (74, bar4_start + 0.0, 0.25),  # D3
    (73, bar4_start + 0.0, 0.25),  # F3
    (74, bar4_start + 0.0, 0.25),  # G3 (resolve)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, C, Bb (Fm7 to Bb)
# Bar 2: Start the motif
# Bar 3: Leave it hanging
# Bar 4: Finish it

sax_notes = [
    # Bar 2: Start motif
    (65, bar2_start + 0.0, 0.25),  # F3
    (68, bar2_start + 0.25, 0.25),  # Ab3
    (67, bar2_start + 0.5, 0.25),  # C4
    (71, bar2_start + 0.75, 0.25),  # Bb4

    # Bar 3: Leave it hanging
    (71, bar3_start + 0.0, 0.25),  # Bb4 (staccato)

    # Bar 4: Finish it
    (65, bar4_start + 0.0, 0.25),  # F3
    (68, bar4_start + 0.25, 0.25),  # Ab3
    (67, bar4_start + 0.5, 0.25),  # C4
    (71, bar4_start + 0.75, 0.25),  # Bb4 (resolve)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums in bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(start_time):
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.0, end=start_time + 0.25)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.25, end=start_time + 0.5)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.0, end=start_time + 0.5)
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.append(hihat)

    kick = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 1.0)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.0, end=start_time + 1.25)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.5, end=start_time + 1.0)
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.append(hihat)

add_drums(bar2_start)
add_drums(bar3_start)
add_drums(bar4_start)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')
