
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 0.75), (38, 0.875), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125),
    (42, 1.25), (42, 1.375), (42, 1.5)
]
for note_number, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (Diatonic root), Bb2 (fifth), Ab2 (chromatic approach)
bass_notes = [
    (53, 1.5, 1.75),  # F2
    (50, 1.75, 2.0),  # Bb2
    (49, 2.0, 2.25),  # Ab2
    (53, 2.25, 2.5)   # F2
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (53, 1.5, 1.75), (60, 1.5, 1.75), (57, 1.5, 1.75), (61, 1.5, 1.75),
    (53, 1.75, 2.0), (60, 1.75, 2.0), (57, 1.75, 2.0), (61, 1.75, 2.0)
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=pitch, start=start, end=end))

# Sax: Opening motif - short, singable, hanging
sax_notes = [
    (57, 1.5, 1.625),  # G (Fm3)
    (59, 1.625, 1.75), # Bb (Fm7)
    (57, 1.75, 1.875), # G
    (55, 1.875, 2.0)   # E (Fm9)
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: D2 (chromatic approach), C2 (root), Bb2 (fifth), Ab2 (chromatic approach)
bass_notes = [
    (50, 3.0, 3.25),  # D2
    (52, 3.25, 3.5),  # C2
    (50, 3.5, 3.75),  # Bb2
    (49, 3.75, 4.0)   # Ab2
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Piano: Bb7 (Bb, D, F, Ab)
piano_notes = [
    (58, 3.0, 3.25), (62, 3.0, 3.25), (53, 3.0, 3.25), (57, 3.0, 3.25),
    (58, 3.25, 3.5), (62, 3.25, 3.5), (53, 3.25, 3.5), (57, 3.25, 3.5)
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=pitch, start=start, end=end))

# Sax: Continue motif, rest on last note
sax_notes = [
    (55, 3.0, 3.125),  # E (Fm9)
    (57, 3.125, 3.25), # G (Fm3)
    (55, 3.25, 3.375), # E
    (55, 3.375, 3.5)   # E (hold)
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F2 (root), D2 (chromatic), C2 (root), Bb2 (fifth)
bass_notes = [
    (53, 4.5, 4.75),  # F2
    (50, 4.75, 5.0),  # D2
    (52, 5.0, 5.25),  # C2
    (50, 5.25, 5.5)   # Bb2
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Piano: Fm7 (F, Ab, C, D)
piano_notes = [
    (53, 4.5, 4.75), (57, 4.5, 4.75), (60, 4.5, 4.75), (61, 4.5, 4.75),
    (53, 4.75, 5.0), (57, 4.75, 5.0), (60, 4.75, 5.0), (61, 4.75, 5.0)
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=pitch, start=start, end=end))

# Sax: Motif return, end on Bb (Fm7)
sax_notes = [
    (57, 4.5, 4.625),  # G (Fm3)
    (59, 4.625, 4.75), # Bb (Fm7)
    (57, 4.75, 4.875), # G
    (59, 4.875, 5.0)   # Bb (Fm7)
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.625), (42, 4.75), (42, 4.875),
    (36, 5.0), (38, 5.375), (42, 5.0), (42, 5.125), (42, 5.25), (42, 5.375),
    (42, 5.5), (42, 5.625), (42, 5.75), (42, 5.875)
]
for note_number, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
