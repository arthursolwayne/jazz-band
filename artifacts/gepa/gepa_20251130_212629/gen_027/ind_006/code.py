
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
    # Bar 1
    (36, 0.0, 0.375),   # Kick on 1
    (38, 0.75, 0.375),  # Snare on 2
    (42, 0.0, 0.1875),  # Hihat on 1
    (42, 0.1875, 0.1875),  # Hihat on &
    (42, 0.375, 0.1875),  # Hihat on 2
    (42, 0.5625, 0.1875), # Hihat on &
    (42, 0.75, 0.1875),  # Hihat on 3
    (42, 0.9375, 0.1875), # Hihat on &
    (42, 1.125, 0.1875), # Hihat on 4
    (42, 1.3125, 0.1875), # Hihat on &
    (36, 1.5, 0.375),    # Kick on 3
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (48, 1.5, 0.375),   # F
    (49, 1.875, 0.375), # G
    (47, 2.25, 0.375),  # E
    (48, 2.625, 0.375), # F
    # Bar 3 (3.0 - 4.5s)
    (50, 3.0, 0.375),   # A
    (51, 3.375, 0.375), # Bb
    (49, 3.75, 0.375),  # G
    (50, 4.125, 0.375), # A
    # Bar 4 (4.5 - 6.0s)
    (52, 4.5, 0.375),   # C
    (53, 4.875, 0.375), # Db
    (51, 5.25, 0.375),  # Bb
    (52, 5.625, 0.375), # C
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.875, 0.1875), # F7 (F, A, C, E)
    (64, 1.875, 0.1875),
    (67, 1.875, 0.1875),
    (69, 1.875, 0.1875),
    # Bar 3 (3.0 - 4.5s)
    (62, 3.375, 0.1875),
    (64, 3.375, 0.1875),
    (67, 3.375, 0.1875),
    (69, 3.375, 0.1875),
    # Bar 4 (4.5 - 6.0s)
    (62, 5.25, 0.1875),
    (64, 5.25, 0.1875),
    (67, 5.25, 0.1875),
    (69, 5.25, 0.1875),
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax - motif with space and rests
sax_notes = [
    # Bar 2 - Motif
    (66, 1.5, 0.1875),   # F
    (69, 1.6875, 0.1875), # A
    (67, 1.875, 0.1875),  # G
    (66, 2.0625, 0.375),  # F (rest until 2.4375)
    (66, 2.4375, 0.1875), # F
    (69, 2.625, 0.1875),  # A
    (67, 2.8125, 0.1875), # G
    (66, 3.0, 0.1875),    # F
    # Bar 3 - Leave it hanging
    (68, 3.0, 0.1875),    # G
    (71, 3.1875, 0.1875), # Bb
    (69, 3.375, 0.1875),  # A
    (70, 3.5625, 0.1875), # B
    (68, 3.75, 0.1875),   # G
    # Bar 4 - Return to motif with variation
    (66, 4.5, 0.1875),    # F
    (69, 4.6875, 0.1875), # A
    (67, 4.875, 0.1875),  # G
    (66, 5.0625, 0.375),  # F (rest until 5.4375)
    (66, 5.4375, 0.1875), # F
    (69, 5.625, 0.1875),  # A
    (67, 5.8125, 0.1875), # G
    (66, 6.0, 0.0),       # Rest
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 0.75, end=bar_start + 0.75 + 0.375))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=bar_start + 1.5, end=bar_start + 1.5 + 0.375))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 2.25, end=bar_start + 2.25 + 0.375))
    # Hihat every eighth
    for i in range(8):
        hihat_start = bar_start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=95, pitch=42, start=hihat_start, end=hihat_start + 0.1875))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")
