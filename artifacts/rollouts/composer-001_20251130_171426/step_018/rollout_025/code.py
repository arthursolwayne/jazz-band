
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

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.125),  # Hihat
    (42, 0.125, 0.125),  # Hihat
    (42, 0.25, 0.125),  # Hihat
    (42, 0.375, 0.125),  # Hihat
    (38, 0.5, 0.375),  # Snare on 2
    (42, 0.5, 0.125),  # Hihat
    (42, 0.625, 0.125),  # Hihat
    (42, 0.75, 0.125),  # Hihat
    (42, 0.875, 0.125),  # Hihat
    (36, 1.0, 0.375),  # Kick on 3
    (42, 1.0, 0.125),  # Hihat
    (42, 1.125, 0.125),  # Hihat
    (42, 1.25, 0.125),  # Hihat
    (42, 1.375, 0.125),  # Hihat
    (38, 1.5, 0.375),  # Snare on 4
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice.
# F bass line: F, Gb, G, Ab, A, Bb, B, C, etc.
bass_notes = [
    (64, 1.5, 0.375),  # F
    (65, 1.875, 0.375),  # Gb
    (67, 2.25, 0.375),  # G
    (68, 2.625, 0.375),  # Ab
    (69, 3.0, 0.375),  # A
    (70, 3.375, 0.375),  # Bb
    (71, 3.75, 0.375),  # B
    (72, 4.125, 0.375),  # C
    (74, 4.5, 0.375),  # D
    (75, 4.875, 0.375),  # Eb
    (76, 5.25, 0.375),  # E
    (77, 5.625, 0.375),  # F
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: 7th chords, comp on 2 and 4
# F7 on 2, Bb7 on 4
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    (64, 1.5, 0.375),  # F
    (69, 1.5, 0.375),  # A
    (72, 1.5, 0.375),  # C
    (68, 1.5, 0.375),  # Eb
    # Bar 3: Rest
    # Bar 4: Bb7 (Bb, D, F, Ab)
    (70, 4.5, 0.375),  # Bb
    (74, 4.5, 0.375),  # D
    (64, 4.5, 0.375),  # F
    (68, 4.5, 0.375),  # Ab
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - C - Eb (F7) with a slight syncopation
sax_notes = [
    (64, 1.5, 0.125),  # F
    (68, 1.625, 0.125),  # Bb
    (72, 1.75, 0.125),  # C
    (68, 1.875, 0.125),  # Eb (leave it hanging)
    # Repeat motif with slight variation
    (64, 2.75, 0.125),  # F
    (68, 2.875, 0.125),  # Bb
    (72, 3.0, 0.125),  # C
    (68, 3.125, 0.125),  # Eb
    # Final resolution
    (64, 4.0, 0.5),  # F (hold for resolution)
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Add drum fills for bars 2-4
# Hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(0, 8):
        dr = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(dr)

# Add snare on 2 and 4 of each bar
for bar in range(2, 5):
    start = bar * 1.5
    snare_times = [start + 0.5, start + 1.5, start + 2.5, start + 3.5]
    for time in snare_times:
        dr = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.375)
        drums.notes.append(dr)

# Add kick on 1 and 3 of each bar
for bar in range(2, 5):
    start = bar * 1.5
    kick_times = [start, start + 1.0, start + 2.0, start + 3.0]
    for time in kick_times:
        dr = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
        drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
