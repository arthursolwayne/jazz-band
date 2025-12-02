
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.375, 0.125),  # Hihat on &1
    (38, 0.75, 0.375),   # Snare on 2
    (42, 0.875, 0.125),  # Hihat on &2
    (36, 1.125, 0.375),  # Kick on 3
    (42, 1.5, 0.125)     # Hihat on &3
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (31, 1.5, 0.375),    # D♭ (Fm7)
    (30, 1.875, 0.375),  # C (chromatic approach)
    (31, 2.25, 0.375),   # D♭ (Fm7)
    (33, 2.625, 0.375),  # E♭ (Fm7)
    (31, 2.875, 0.375),  # D♭ (Fm7)
    (30, 3.25, 0.375),   # C (chromatic approach)
    (31, 3.625, 0.375),  # D♭ (Fm7)
    (33, 4.0, 0.375),    # E♭ (Fm7)
    (31, 4.375, 0.375),  # D♭ (Fm7)
    (30, 4.75, 0.375),   # C (chromatic approach)
    (31, 5.125, 0.375),  # D♭ (Fm7)
    (33, 5.5, 0.375)     # E♭ (Fm7)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (48, 1.5, 0.375),    # Fm7 (F, Ab, C, D♭)
    (50, 1.5, 0.375),
    (52, 1.5, 0.375),
    (53, 1.5, 0.375),
    (50, 1.875, 0.375),  # C (comp)
    (52, 1.875, 0.375),
    (53, 1.875, 0.375),
    (48, 2.25, 0.375),   # Fm7 (F, Ab, C, D♭)
    (50, 2.25, 0.375),
    (52, 2.25, 0.375),
    (53, 2.25, 0.375),
    (50, 2.625, 0.375),  # C (comp)
    (52, 2.625, 0.375),
    (53, 2.625, 0.375),
    (48, 3.0, 0.375),    # Fm7 (F, Ab, C, D♭)
    (50, 3.0, 0.375),
    (52, 3.0, 0.375),
    (53, 3.0, 0.375),
    (50, 3.375, 0.375),  # C (comp)
    (52, 3.375, 0.375),
    (53, 3.375, 0.375),
    (48, 3.75, 0.375),   # Fm7 (F, Ab, C, D♭)
    (50, 3.75, 0.375),
    (52, 3.75, 0.375),
    (53, 3.75, 0.375),
    (50, 4.125, 0.375),  # C (comp)
    (52, 4.125, 0.375),
    (53, 4.125, 0.375),
    (48, 4.5, 0.375),    # Fm7 (F, Ab, C, D♭)
    (50, 4.5, 0.375),
    (52, 4.5, 0.375),
    (53, 4.5, 0.375),
    (50, 4.875, 0.375),  # C (comp)
    (52, 4.875, 0.375),
    (53, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.5, end=start + 1.875))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 2.25, end=start + 2.625))
    # Hihat on every eighth
    for i in range(0, 8):
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125))

# Sax: Your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: Fm, whisper at first, then a cry
sax_notes = [
    (53, 1.5, 0.25),     # D♭ (whisper)
    (51, 1.75, 0.25),    # B♭ (whisper)
    (50, 2.0, 0.25),     # A (whisper)
    (53, 2.25, 0.25),    # D♭ (cry)
    (55, 2.5, 0.25),     # E (cry)
    (57, 2.75, 0.25),    # F (cry)
    (55, 3.0, 0.25),     # E (cry)
    (53, 3.25, 0.25),    # D♭ (cry)
    (51, 3.5, 0.25),     # B♭ (cry)
    (50, 3.75, 0.25),    # A (cry)
    (53, 4.0, 0.25),     # D♭ (cry)
    (55, 4.25, 0.25),    # E (cry)
    (57, 4.5, 0.25),     # F (cry)
    (55, 4.75, 0.25),    # E (cry)
    (53, 5.0, 0.25),     # D♭ (cry)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_4bar.mid")
