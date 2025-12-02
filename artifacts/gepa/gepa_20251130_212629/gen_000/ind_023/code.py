
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.1875, 0.1875), # Hihat on &1
    (38, 0.75, 0.375),   # Snare on 2
    (42, 0.9375, 0.1875), # Hihat on &2
    (36, 1.125, 0.375),  # Kick on 3
    (42, 1.3125, 0.1875), # Hihat on &3
    (38, 1.875, 0.375),  # Snare on 4
    (42, 2.0625, 0.1875) # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Fm
bass_notes = [
    (64, 1.5, 0.375),   # F
    (62, 1.875, 0.375),  # D
    (60, 2.25, 0.375),   # C
    (64, 2.625, 0.375)   # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 - Fm7 on beat 1
    (64, 1.5, 0.1875),   # F
    (67, 1.5, 0.1875),   # A
    (64, 1.5, 0.1875),   # F
    (70, 1.5, 0.1875),   # C
    (69, 1.5, 0.1875),   # Bb
    # Bar 2 - Fm7 on beat 3
    (64, 2.25, 0.1875),  # F
    (67, 2.25, 0.1875),  # A
    (64, 2.25, 0.1875),  # F
    (70, 2.25, 0.1875),  # C
    (69, 2.25, 0.1875),  # Bb
    # Bar 3 - Fm7 on beat 1
    (64, 3.0, 0.1875),   # F
    (67, 3.0, 0.1875),   # A
    (64, 3.0, 0.1875),   # F
    (70, 3.0, 0.1875),   # C
    (69, 3.0, 0.1875),   # Bb
    # Bar 3 - Fm7 on beat 3
    (64, 3.75, 0.1875),  # F
    (67, 3.75, 0.1875),  # A
    (64, 3.75, 0.1875),  # F
    (70, 3.75, 0.1875),  # C
    (69, 3.75, 0.1875),  # Bb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.6875, 0.1875), # Hihat on &1
    (38, 1.875, 0.375),   # Snare on 2
    (42, 2.0625, 0.1875), # Hihat on &2
    (36, 2.25, 0.375),    # Kick on 3
    (42, 2.4375, 0.1875), # Hihat on &3
    (38, 2.625, 0.375),   # Snare on 4
    (42, 2.8125, 0.1875), # Hihat on &4
    (36, 3.0, 0.375),     # Kick on 1
    (42, 3.1875, 0.1875), # Hihat on &1
    (38, 3.375, 0.375),   # Snare on 2
    (42, 3.5625, 0.1875), # Hihat on &2
    (36, 3.75, 0.375),    # Kick on 3
    (42, 3.9375, 0.1875), # Hihat on &3
    (38, 4.125, 0.375),   # Snare on 4
    (42, 4.3125, 0.1875), # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing
# Start on F (64), then Gb (65), then Ab (67), then F (64)
sax_notes = [
    (64, 1.5, 0.1875),   # F
    (65, 1.6875, 0.1875), # Gb
    (67, 1.875, 0.1875),  # Ab
    (64, 2.0625, 0.1875)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm
bass_notes = [
    (62, 3.0, 0.375),    # D
    (60, 3.375, 0.375),   # C
    (62, 3.75, 0.375),    # D
    (64, 4.125, 0.375)    # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3 - Fm7 on beat 1
    (64, 3.0, 0.1875),  # F
    (67, 3.0, 0.1875),  # A
    (64, 3.0, 0.1875),  # F
    (70, 3.0, 0.1875),  # C
    (69, 3.0, 0.1875),  # Bb
    # Bar 3 - Fm7 on beat 3
    (64, 3.75, 0.1875), # F
    (67, 3.75, 0.1875), # A
    (64, 3.75, 0.1875), # F
    (70, 3.75, 0.1875), # C
    (69, 3.75, 0.1875), # Bb
    # Bar 4 - Fm7 on beat 1
    (64, 4.5, 0.1875),   # F
    (67, 4.5, 0.1875),   # A
    (64, 4.5, 0.1875),   # F
    (70, 4.5, 0.1875),   # C
    (69, 4.5, 0.1875),   # Bb
    # Bar 4 - Fm7 on beat 3
    (64, 4.875, 0.1875), # F
    (67, 4.875, 0.1875), # A
    (64, 4.875, 0.1875), # F
    (70, 4.875, 0.1875), # C
    (69, 4.875, 0.1875)  # Bb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.1875, 0.1875), # Hihat on &1
    (38, 3.375, 0.375),   # Snare on 2
    (42, 3.5625, 0.1875), # Hihat on &2
    (36, 3.75, 0.375),    # Kick on 3
    (42, 3.9375, 0.1875), # Hihat on &3
    (38, 4.125, 0.375),   # Snare on 4
    (42, 4.3125, 0.1875), # Hihat on &4
    (36, 4.5, 0.375),     # Kick on 1
    (42, 4.6875, 0.1875), # Hihat on &1
    (38, 4.875, 0.375),   # Snare on 2
    (42, 5.0625, 0.1875), # Hihat on &2
    (36, 5.25, 0.375),    # Kick on 3
    (42, 5.4375, 0.1875), # Hihat on &3
    (38, 5.625, 0.375),   # Snare on 4
    (42, 5.8125, 0.1875)  # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Finish the motif
# Start on F (64), then Gb (65), then Ab (67), then F (64)
sax_notes = [
    (64, 4.5, 0.1875),   # F
    (65, 4.6875, 0.1875), # Gb
    (67, 4.875, 0.1875),  # Ab
    (64, 5.0625, 0.1875)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm
bass_notes = [
    (60, 4.5, 0.375),    # C
    (62, 4.875, 0.375),   # D
    (64, 5.25, 0.375),    # F
    (62, 5.625, 0.375)    # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4 - Fm7 on beat 1
    (64, 4.5, 0.1875),  # F
    (67, 4.5, 0.1875),  # A
    (64, 4.5, 0.1875),  # F
    (70, 4.5, 0.1875),  # C
    (69, 4.5, 0.1875),  # Bb
    # Bar 4 - Fm7 on beat 3
    (64, 5.25, 0.1875), # F
    (67, 5.25, 0.1875), # A
    (64, 5.25, 0.1875), # F
    (70, 5.25, 0.1875), # C
    (69, 5.25, 0.1875), # Bb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.6875, 0.1875), # Hihat on &1
    (38, 4.875, 0.375),   # Snare on 2
    (42, 5.0625, 0.1875), # Hihat on &2
    (36, 5.25, 0.375),    # Kick on 3
    (42, 5.4375, 0.1875), # Hihat on &3
    (38, 5.625, 0.375),   # Snare on 4
    (42, 5.8125, 0.1875)  # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
