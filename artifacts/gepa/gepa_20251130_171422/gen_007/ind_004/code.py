
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
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.1875),  # Hihat on 1
    (42, 0.1875, 0.1875),  # Hihat on &
    (42, 0.375, 0.1875),  # Hihat on 2
    (42, 0.5625, 0.1875),  # Hihat on &
    (42, 0.75, 0.1875),  # Hihat on 3
    (42, 0.9375, 0.1875),  # Hihat on &
    (36, 1.125, 0.375),  # Kick on 3
    (38, 1.5, 0.375),  # Snare on 4
    (42, 1.125, 0.1875),  # Hihat on 3
    (42, 1.3125, 0.1875),  # Hihat on &
    (42, 1.5, 0.1875)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375),  # Eb
    (64, 2.25, 0.375),  # E
    (62, 2.625, 0.375),  # D
    (60, 2.875, 0.375),  # C
    (62, 3.25, 0.375),  # D
    (65, 3.625, 0.375),  # F
    (64, 4.0, 0.375),  # E
    (62, 4.375, 0.375),  # D
    (63, 4.75, 0.375),  # Eb
    (64, 5.125, 0.375),  # E
    (62, 5.5, 0.375)  # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.5, 0.375),  # D7 - D
    (67, 1.5, 0.375),  # D7 - A
    (64, 1.5, 0.375),  # D7 - E
    (67, 1.5, 0.375),  # D7 - A
    # Bar 3
    (62, 2.625, 0.375),  # D7 - D
    (67, 2.625, 0.375),  # D7 - A
    (64, 2.625, 0.375),  # D7 - E
    (67, 2.625, 0.375),  # D7 - A
    # Bar 4
    (62, 3.625, 0.375),  # D7 - D
    (67, 3.625, 0.375),  # D7 - A
    (64, 3.625, 0.375),  # D7 - E
    (67, 3.625, 0.375),  # D7 - A
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif - D, F, Eb, D (start at 1.5s)
sax_notes = [
    (62, 1.5, 0.375),  # D
    (65, 1.875, 0.375),  # F
    (63, 2.25, 0.375),  # Eb
    (62, 2.625, 0.375)  # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add drum fills for bar 2-4
# Bar 2 (1.5 - 3.0s) - Hi-hat on every 8th, kick on 1 and 3
for i in range(4):
    hihat_start = 1.5 + i * 0.375
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.1875)
    drums.notes.append(hihat)

kick_start = 1.5
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375))
kick_start = 1.5 + 1.5
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375))

# Bar 3 (3.0 - 4.5s) - Snare on 2 and 4
snare_start = 3.375
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375))
snare_start = 4.5
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375))

# Bar 4 (4.5 - 6.0s) - Kick on 1 and 3, snare on 2 and 4
kick_start = 4.5
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375))
kick_start = 4.5 + 1.5
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375))
snare_start = 4.875
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375))
snare_start = 6.0
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375))

# Add hi-hats to fill the bar
for i in range(6):
    hihat_start = 4.5 + i * 0.375
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.1875)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
