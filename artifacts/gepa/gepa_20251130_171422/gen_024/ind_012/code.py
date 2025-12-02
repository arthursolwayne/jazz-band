
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
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on &1
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875), # Hihat on &2
    (42, 0.75, 0.1875), # Hihat on 3
    (42, 0.9375, 0.1875), # Hihat on &3
    (42, 1.125, 0.1875), # Hihat on 4
    (42, 1.3125, 0.1875), # Hihat on &4
    (36, 1.5, 0.375),   # Kick on 3
    (38, 1.5, 0.375),   # Snare on 4 (overlapping kick)
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet enters (1.5 - 3.0s)

# Marcus (Bass): Walking line in Fm
bass_notes = [
    (63, 1.5, 0.375),  # F (root)
    (61, 1.875, 0.375), # Eb (chromatic approach)
    (64, 2.25, 0.375),  # Gb (chromatic approach)
    (62, 2.625, 0.375), # E (3rd)
]

for note, start, duration in bass_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Diane (Piano): 7th chords on 2 and 4
piano_notes = [
    (64, 2.25, 0.375), # F7 (F, A, C, Eb)
    (64, 2.25, 0.375),
    (69, 2.25, 0.375),
    (60, 2.25, 0.375),
    (62, 2.625, 0.375), # Bb7 (Bb, D, F, Ab)
    (62, 2.625, 0.375),
    (67, 2.625, 0.375),
    (60, 2.625, 0.375)
]

for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Dante (Sax): One short motif, sparse but expressive
sax_notes = [
    (61, 1.875, 0.1875), # Eb (start on &2)
    (64, 2.25, 0.375),  # Gb
    (62, 2.625, 0.1875), # E
    (61, 2.8125, 0.1875), # Eb
]

for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Drums continue in bar 2
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.5, 0.1875), # Hihat on 1
    (42, 1.6875, 0.1875), # Hihat on &1
    (42, 1.875, 0.1875), # Hihat on 2
    (42, 2.0625, 0.1875), # Hihat on &2
    (42, 2.25, 0.1875), # Hihat on 3
    (42, 2.4375, 0.1875), # Hihat on &3
    (42, 2.625, 0.1875), # Hihat on 4
    (42, 2.8125, 0.1875), # Hihat on &4
    (36, 3.0, 0.375),   # Kick on 3
    (38, 3.0, 0.375),   # Snare on 4 (overlapping kick)
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 3: Marcus continues walking
bass_notes = [
    (65, 3.0, 0.375),  # Ab (chromatic approach)
    (66, 3.375, 0.375), # A (chromatic approach)
    (63, 3.75, 0.375),  # F (root)
    (61, 4.125, 0.375), # Eb (chromatic approach)
]

for note, start, duration in bass_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Diane continues comping
piano_notes = [
    (65, 3.375, 0.375), # Ab (F7)
    (65, 3.375, 0.375),
    (69, 3.375, 0.375),
    (60, 3.375, 0.375),
    (62, 3.75, 0.375), # Bb7
    (62, 3.75, 0.375),
    (67, 3.75, 0.375),
    (60, 3.75, 0.375)
]

for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Dante: Continue motif
sax_notes = [
    (64, 3.375, 0.1875), # Gb
    (62, 3.5625, 0.1875), # E
    (61, 3.75, 0.1875), # Eb
    (60, 3.9375, 0.1875), # D (pushing the tension)
]

for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Drums continue in bar 3
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.0, 0.1875), # Hihat on 1
    (42, 3.1875, 0.1875), # Hihat on &1
    (42, 3.375, 0.1875), # Hihat on 2
    (42, 3.5625, 0.1875), # Hihat on &2
    (42, 3.75, 0.1875), # Hihat on 3
    (42, 3.9375, 0.1875), # Hihat on &3
    (42, 4.125, 0.1875), # Hihat on 4
    (42, 4.3125, 0.1875), # Hihat on &4
    (36, 4.5, 0.375),   # Kick on 3
    (38, 4.5, 0.375),   # Snare on 4 (overlapping kick)
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 4: Marcus continues
bass_notes = [
    (62, 4.5, 0.375),  # Eb (chromatic approach)
    (64, 4.875, 0.375), # Gb (chromatic approach)
    (62, 5.25, 0.375), # Eb
    (60, 5.625, 0.375), # D (pushing tension)
]

for note, start, duration in bass_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Diane continues comping
piano_notes = [
    (62, 4.875, 0.375), # Bb7
    (62, 4.875, 0.375),
    (67, 4.875, 0.375),
    (60, 4.875, 0.375),
    (64, 5.25, 0.375), # F7
    (64, 5.25, 0.375),
    (69, 5.25, 0.375),
    (60, 5.25, 0.375)
]

for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Dante: Resolve the motif
sax_notes = [
    (60, 5.25, 0.1875), # D
    (62, 5.4375, 0.1875), # Eb
    (64, 5.625, 0.1875), # Gb
    (65, 5.8125, 0.1875), # Ab (closing tension)
]

for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Drums continue in bar 4
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.5, 0.1875), # Hihat on 1
    (42, 4.6875, 0.1875), # Hihat on &1
    (42, 4.875, 0.1875), # Hihat on 2
    (42, 5.0625, 0.1875), # Hihat on &2
    (42, 5.25, 0.1875), # Hihat on 3
    (42, 5.4375, 0.1875), # Hihat on &3
    (42, 5.625, 0.1875), # Hihat on 4
    (42, 5.8125, 0.1875), # Hihat on &4
    (36, 6.0, 0.375),   # Kick on 3
    (38, 6.0, 0.375),   # Snare on 4 (overlapping kick)
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

# Save to MIDI file
midi.write("jazz_intro.mid")
