
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
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.1875),  # Hihat on 1
    (42, 0.1875, 0.1875),  # Hihat on &
    (42, 0.375, 0.1875),  # Hihat on 2
    (42, 0.5625, 0.1875),  # Hihat on &
    (42, 0.75, 0.1875),  # Hihat on 3
    (42, 0.9375, 0.1875),  # Hihat on &
    (42, 1.125, 0.1875),  # Hihat on 4
    (36, 1.125, 0.375),  # Kick on 3
    (38, 1.5, 0.375),  # Snare on 4
]

for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),  # F (root)
    (40, 1.875, 0.375),  # Ab (chromatic approach)
    (43, 2.25, 0.375),  # C (fifth)
    (41, 2.625, 0.375),  # Bb (chromatic approach)
    (38, 2.625, 0.375),  # F (root)
    (40, 3.0, 0.375),  # Ab (chromatic approach)
    (43, 3.375, 0.375),  # C (fifth)
    (41, 3.75, 0.375),  # Bb (chromatic approach)
    (38, 3.75, 0.375),  # F (root)
    (40, 4.125, 0.375),  # Ab (chromatic approach)
    (43, 4.5, 0.375),  # C (fifth)
    (41, 4.875, 0.375),  # Bb (chromatic approach)
]

for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, Eb)
piano_notes = [
    (65, 1.5, 0.375),  # F
    (68, 1.5, 0.375),  # A
    (72, 1.5, 0.375),  # C
    (67, 1.5, 0.375),  # Eb

    # Bar 3: Gm7 (G, Bb, D, F)
    (67, 2.25, 0.375),  # G
    (69, 2.25, 0.375),  # Bb
    (72, 2.25, 0.375),  # D
    (72, 2.25, 0.375),  # F (duplicate for emphasis)

    # Bar 4: Cm7 (C, Eb, G, Bb)
    (72, 3.0, 0.375),  # C
    (67, 3.0, 0.375),  # Eb
    (72, 3.0, 0.375),  # G (duplicate for emphasis)
    (69, 3.0, 0.375),  # Bb
]

for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F, Ab, Bb (F7), then rest on the & of 2, come back with Bb, F (resolution)
sax_notes = [
    (65, 1.5, 0.375),  # F
    (67, 1.875, 0.375),  # Ab
    (69, 2.25, 0.375),  # Bb
    (69, 2.625, 0.375),  # Bb (rest on & of 2)
    (69, 3.0, 0.375),  # Bb
    (65, 3.375, 0.375),  # F
]

for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

# Drums: Continue in bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = bar * 1.5
    drum_notes = [
        (36, start_time, 0.375),  # Kick on 1
        (38, start_time + 0.375, 0.375),  # Snare on 2
        (42, start_time, 0.1875),  # Hihat on 1
        (42, start_time + 0.1875, 0.1875),  # Hihat on &
        (42, start_time + 0.375, 0.1875),  # Hihat on 2
        (42, start_time + 0.5625, 0.1875),  # Hihat on &
        (42, start_time + 0.75, 0.1875),  # Hihat on 3
        (42, start_time + 0.9375, 0.1875),  # Hihat on &
        (42, start_time + 1.125, 0.1875),  # Hihat on 4
        (36, start_time + 1.125, 0.375),  # Kick on 3
        (38, start_time + 1.5, 0.375),  # Snare on 4
    ]
    for note_number, note_start, duration in drum_notes:
        note = pretty_midi.Note(velocity=100, pitch=note_number, start=note_start, end=note_start + duration)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.save('dante_intro.mid')
