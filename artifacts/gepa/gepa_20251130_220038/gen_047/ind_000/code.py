
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.375, 0.125),  # Hihat on 1&2
    (38, 0.75, 0.375),   # Snare on 2
    (42, 0.75, 0.125),   # Hihat on 2&3
    (36, 1.125, 0.375),  # Kick on 3
    (42, 1.125, 0.125),  # Hihat on 3&4
    (38, 1.5, 0.375)     # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: chromatic walking line with approach patterns
bass_notes = [
    (37, 1.5, 0.375),    # F# (chromatic up)
    (39, 1.875, 0.375),  # A (diatonic)
    (41, 2.25, 0.375),   # B (diatonic)
    (42, 2.625, 0.375),  # C (diatonic)
    (43, 2.625, 0.375),  # C# (chromatic up)
    (45, 3.0, 0.375),    # D# (chromatic up)
    (47, 3.375, 0.375),  # F (diatonic)
    (48, 3.75, 0.375),   # F# (diatonic)
    (50, 4.125, 0.375),  # A (diatonic)
    (52, 4.5, 0.375),    # B (diatonic)
    (53, 4.875, 0.375),  # C (diatonic)
    (55, 5.25, 0.375),   # D# (chromatic up)
    (57, 5.625, 0.375),  # F (diatonic)
    (58, 6.0, 0.375)     # F# (diatonic)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comping on 2 and 4
piano_notes = [
    (50, 1.875, 0.125),  # A7 (50=A, 48=F#, 46=C)
    (48, 1.875, 0.125),
    (46, 1.875, 0.125),
    (50, 3.0, 0.125),    # A7
    (48, 3.0, 0.125),
    (46, 3.0, 0.125),
    (50, 4.5, 0.125),    # A7
    (48, 4.5, 0.125),
    (46, 4.5, 0.125)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25))
    # Hihat on every eighth
    for i in range(4):
        hihat_start = bar_start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.125))

# Sax melody: short motif, start it, leave it hanging, come back and finish it
# Motif: F (53) - G (55) - Bb (50) - F (53)
# Start in bar 2, leave it hanging, then come back in bar 4

# Bar 2
sax.notes.append(pretty_midi.Note(velocity=105, pitch=53, start=1.5, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=105, pitch=55, start=1.75, end=2.0))

# Bar 3: silence

# Bar 4
sax.notes.append(pretty_midi.Note(velocity=105, pitch=50, start=4.5, end=4.75))
sax.notes.append(pretty_midi.Note(velocity=105, pitch=53, start=4.75, end=5.0))

# Final note to linger
sax.notes.append(pretty_midi.Note(velocity=105, pitch=53, start=5.0, end=5.25))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_shorter_intro.mid")
