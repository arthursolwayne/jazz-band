
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
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass (walking line with chromatic approaches)
bass_notes = [
    (48, 1.5, 0.375),  # F3
    (50, 1.875, 0.375),  # G#3 (chromatic approach)
    (49, 2.25, 0.375),  # A3
    (51, 2.625, 0.375),  # Bb3
    (51, 2.625, 0.375),  # Bb3 (hold)
    (50, 3.0, 0.375),  # G#3
    (48, 3.375, 0.375),  # F3
    (49, 3.75, 0.375),  # A3
    (51, 4.125, 0.375),  # Bb3
    (52, 4.5, 0.375),  # B3
    (51, 4.875, 0.375),  # Bb3
    (50, 5.25, 0.375),  # G#3
    (48, 5.625, 0.375),  # F3
    (49, 6.0, 0.375),  # A3 (end of bar 4)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane - Piano (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (59, 1.5, 0.375),  # C7 (F7 chord)
    (62, 1.5, 0.375),
    (64, 1.5, 0.375),
    (60, 1.5, 0.375),
    (61, 1.5, 0.375),
    (63, 1.5, 0.375),
    (59, 1.875, 0.375),  # C7
    (62, 1.875, 0.375),
    (64, 1.875, 0.375),
    (60, 1.875, 0.375),
    (61, 1.875, 0.375),
    (63, 1.875, 0.375),
    # Bar 3 (3.0 - 4.5s)
    (60, 3.0, 0.375),  # F7
    (62, 3.0, 0.375),
    (64, 3.0, 0.375),
    (65, 3.0, 0.375),
    (61, 3.0, 0.375),
    (63, 3.0, 0.375),
    (60, 3.375, 0.375),  # F7
    (62, 3.375, 0.375),
    (64, 3.375, 0.375),
    (65, 3.375, 0.375),
    (61, 3.375, 0.375),
    (63, 3.375, 0.375),
    # Bar 4 (4.5 - 6.0s)
    (60, 4.5, 0.375),  # F7
    (62, 4.5, 0.375),
    (64, 4.5, 0.375),
    (65, 4.5, 0.375),
    (61, 4.5, 0.375),
    (63, 4.5, 0.375),
    (60, 4.875, 0.375),  # F7
    (62, 4.875, 0.375),
    (64, 4.875, 0.375),
    (65, 4.875, 0.375),
    (61, 4.875, 0.375),
    (63, 4.875, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray - Drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 0.75 + 0.375)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.375 + 0.375)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.125 + 0.375)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.375 + 0.375)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 0.75 + 0.375)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.125 + 0.375)
    # Add to drum instrument
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Dante - Sax (tenor, 1 short motif, sing it, leave it hanging)
sax_notes = [
    (66, 1.5, 0.375),  # A4
    (69, 1.875, 0.375),  # C5
    (67, 2.25, 0.375),  # Bb4
    (66, 2.625, 0.375),  # A4
    (65, 3.0, 0.375),  # G4
    (67, 3.375, 0.375),  # Bb4
    (69, 3.75, 0.375),  # C5
    (67, 4.125, 0.375),  # Bb4
    (66, 4.5, 0.375),  # A4
    (65, 4.875, 0.375),  # G4
    (64, 5.25, 0.375),  # F4
    (66, 5.625, 0.375),  # A4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
