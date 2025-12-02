
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
    (36, 0.0, 1.0),   # Kick on 1
    (42, 0.25, 0.25), # Hihat on &1
    (36, 0.75, 1.0),  # Kick on 3
    (42, 0.95, 0.25), # Hihat on &3
    (42, 1.3, 0.25),  # Hihat on 2
    (38, 1.4, 0.25),  # Snare on 4
    (42, 1.5, 0.25)   # Hihat on &4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: G (Bb4), A (Bb4), D (F#4), rest

sax_notes = [
    (74, 1.5, 0.375),  # G (Bb4)
    (76, 1.875, 0.375), # A (Bb4)
    (70, 2.25, 0.375),  # D (F#4)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: walking line in D
bass_notes = [
    (62, 1.5, 0.375),  # D (E3)
    (64, 1.875, 0.375), # E (F3)
    (65, 2.25, 0.375),  # F (F#3)
    (62, 2.625, 0.375)  # D (E3)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (67, 1.875, 0.375),  # D7 (F#3)
    (69, 1.875, 0.375),  # A (B3)
    (64, 1.875, 0.375),  # G (A3)
    (72, 1.875, 0.375),  # C (C4)
    (74, 2.625, 0.375),  # D7 (F#3)
    (76, 2.625, 0.375),  # A (B3)
    (71, 2.625, 0.375),  # G (A3)
    (79, 2.625, 0.375),  # C (C4)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 1.0),   # Kick on 1
    (42, 1.75, 0.25), # Hihat on &1
    (38, 2.0, 0.25),  # Snare on 2
    (42, 2.25, 0.25), # Hihat on &2
    (36, 2.5, 1.0),   # Kick on 3
    (42, 2.75, 0.25), # Hihat on &3
    (38, 3.0, 0.25),  # Snare on 4
    (42, 3.25, 0.25)  # Hihat on &4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif but add a half-step chromatic
sax_notes = [
    (74, 3.0, 0.375),  # G (Bb4)
    (76, 3.375, 0.375), # A (Bb4)
    (70, 3.75, 0.375),  # D (F#4)
    (69, 4.125, 0.375)  # C# (F4)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Walk again, with chromatic approach
bass_notes = [
    (62, 3.0, 0.375),  # D (E3)
    (64, 3.375, 0.375), # E (F3)
    (65, 3.75, 0.375),  # F (F#3)
    (63, 4.125, 0.375)  # E (F3)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (67, 3.375, 0.375),  # D7 (F#3)
    (69, 3.375, 0.375),  # A (B3)
    (64, 3.375, 0.375),  # G (A3)
    (72, 3.375, 0.375),  # C (C4)
    (67, 4.125, 0.375),  # D7 (F#3)
    (69, 4.125, 0.375),  # A (B3)
    (64, 4.125, 0.375),  # G (A3)
    (72, 4.125, 0.375)   # C (C4)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 1.0),   # Kick on 1
    (42, 3.25, 0.25), # Hihat on &1
    (38, 3.5, 0.25),  # Snare on 2
    (42, 3.75, 0.25), # Hihat on &2
    (36, 4.0, 1.0),   # Kick on 3
    (42, 4.25, 0.25), # Hihat on &3
    (38, 4.5, 0.25),  # Snare on 4
    (42, 4.75, 0.25)  # Hihat on &4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End on a rest, leave it hanging
sax_notes = []
# No sax notes: leave it open

# Bass: Walk again, with chromatic approach
bass_notes = [
    (62, 4.5, 0.375),  # D (E3)
    (64, 4.875, 0.375), # E (F3)
    (65, 5.25, 0.375),  # F (F#3)
    (63, 5.625, 0.375)  # E (F3)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (67, 4.875, 0.375),  # D7 (F#3)
    (69, 4.875, 0.375),  # A (B3)
    (64, 4.875, 0.375),  # G (A3)
    (72, 4.875, 0.375),  # C (C4)
    (67, 5.625, 0.375),  # D7 (F#3)
    (69, 5.625, 0.375),  # A (B3)
    (64, 5.625, 0.375),  # G (A3)
    (72, 5.625, 0.375)   # C (C4)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 1.0),   # Kick on 1
    (42, 4.75, 0.25), # Hihat on &1
    (38, 5.0, 0.25),  # Snare on 2
    (42, 5.25, 0.25), # Hihat on &2
    (36, 5.5, 1.0),   # Kick on 3
    (42, 5.75, 0.25), # Hihat on &3
    (38, 6.0, 0.25),  # Snare on 4
    (42, 6.25, 0.25)  # Hihat on &4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
