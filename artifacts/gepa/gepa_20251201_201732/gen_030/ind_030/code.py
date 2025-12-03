
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
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.125, 0.25), # Hihat on 1&
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.5, 0.25),   # Hihat on 2&
    (36, 0.75, 0.375), # Kick on 3
    (42, 0.875, 0.25), # Hihat on 3&
    (38, 1.125, 0.375),# Snare on 4
    (42, 1.25, 0.25)   # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375), # D2 on 1
    (40, 1.875, 0.375), # F2 on 2
    (43, 2.25, 0.375), # A2 on 3
    (42, 2.625, 0.375), # G2 on 4
    (38, 3.0, 0.375), # D2 on 1
    (40, 3.375, 0.375), # F2 on 2
    (43, 3.75, 0.375), # A2 on 3
    (42, 4.125, 0.375), # G2 on 4
    (38, 4.5, 0.375), # D2 on 1
    (40, 4.875, 0.375), # F2 on 2
    (43, 5.25, 0.375), # A2 on 3
    (42, 5.625, 0.375)  # G2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G)
piano_notes = [
    (57, 1.5, 0.375), # F (Dm7)
    (62, 1.5, 0.375), # A
    (67, 1.5, 0.375), # D
    (71, 1.5, 0.375), # G
    (64, 2.25, 0.375), # C (G7)
    (67, 2.25, 0.375), # G
    (72, 2.25, 0.375), # B
    (76, 2.25, 0.375), # D
    (62, 3.0, 0.375), # A (Cm7)
    (67, 3.0, 0.375), # D
    (72, 3.0, 0.375), # F
    (76, 3.0, 0.375), # A
    (64, 3.75, 0.375), # C (F7)
    (67, 3.75, 0.375), # G
    (72, 3.75, 0.375), # B
    (77, 3.75, 0.375)  # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 * bar
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Hihat on 1&
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.125, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125))
    # Hihat on 2&
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.875, end=bar_start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.5, end=bar_start + 1.875))
    # Hihat on 3&
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.625, end=bar_start + 1.875))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 2.25, end=bar_start + 2.625))
    # Hihat on 4&
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 2.375, end=bar_start + 2.625))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.25), # E (Dm7)
    (67, 1.75, 0.25), # Bb (G7)
    (62, 2.0, 0.25), # E (Cm7)
    (67, 2.25, 0.25), # Bb (F7)
    (62, 3.0, 0.25), # E
    (69, 3.25, 0.25), # D (resolve)
    (67, 3.5, 0.25), # Bb
    (64, 3.75, 0.25)  # C (resolve)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
