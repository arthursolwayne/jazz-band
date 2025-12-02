
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.1875),  # Hihat on 1 &
    (42, 0.1875, 0.1875),  # Hihat on 2 &
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875),  # Hihat on 2 &
    (42, 0.5625, 0.1875),  # Hihat on 3 &
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.1875),  # Hihat on 3 &
    (42, 0.9375, 0.1875),  # Hihat on 4 &
    (38, 1.125, 0.375),  # Snare on 4
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus (bass) - walking line in F
bass_notes = [
    (45, 1.5, 0.375), # F3
    (47, 1.875, 0.375), # G3
    (49, 2.25, 0.375), # A3
    (48, 2.625, 0.375), # Ab3
    (45, 2.625, 0.375), # F3
    (47, 3.0, 0.375), # G3
    (49, 3.375, 0.375), # A3
    (48, 3.75, 0.375), # Ab3
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Diane (piano) - comping on 2 and 4
piano_notes = [
    (62, 1.875, 0.375), # F#4 (F7)
    (65, 1.875, 0.375), # A4 (F7)
    (67, 1.875, 0.375), # B4 (F7)
    (69, 1.875, 0.375), # C#5 (F7)
    (62, 3.0, 0.375), # F#4 (F7)
    (65, 3.0, 0.375), # A4 (F7)
    (67, 3.0, 0.375), # B4 (F7)
    (69, 3.0, 0.375), # C#5 (F7)
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Dante (sax) - motif
sax_notes = [
    (66, 1.5, 0.375), # F4
    (68, 1.875, 0.375), # G4
    (69, 2.25, 0.375), # A4
    (66, 2.625, 0.375), # F4
    (66, 3.0, 0.375), # F4
    (68, 3.375, 0.375), # G4
    (69, 3.75, 0.375), # A4
    (66, 4.125, 0.375), # F4
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus (bass) - walking line
bass_notes = [
    (45, 3.0, 0.375), # F3
    (47, 3.375, 0.375), # G3
    (49, 3.75, 0.375), # A3
    (48, 4.125, 0.375), # Ab3
    (45, 4.125, 0.375), # F3
    (47, 4.5, 0.375), # G3
    (49, 4.875, 0.375), # A3
    (48, 5.25, 0.375), # Ab3
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Diane (piano) - comping on 2 and 4
piano_notes = [
    (62, 3.375, 0.375), # F#4 (F7)
    (65, 3.375, 0.375), # A4 (F7)
    (67, 3.375, 0.375), # B4 (F7)
    (69, 3.375, 0.375), # C#5 (F7)
    (62, 4.5, 0.375), # F#4 (F7)
    (65, 4.5, 0.375), # A4 (F7)
    (67, 4.5, 0.375), # B4 (F7)
    (69, 4.5, 0.375), # C#5 (F7)
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Dante (sax) - motif
sax_notes = [
    (66, 3.0, 0.375), # F4
    (68, 3.375, 0.375), # G4
    (69, 3.75, 0.375), # A4
    (66, 4.125, 0.375), # F4
    (66, 4.5, 0.375), # F4
    (68, 4.875, 0.375), # G4
    (69, 5.25, 0.375), # A4
    (66, 5.625, 0.375), # F4
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus (bass) - walking line
bass_notes = [
    (45, 4.5, 0.375), # F3
    (47, 4.875, 0.375), # G3
    (49, 5.25, 0.375), # A3
    (48, 5.625, 0.375), # Ab3
    (45, 5.625, 0.375), # F3
    (47, 6.0, 0.375), # G3
    (49, 6.375, 0.375), # A3
    (48, 6.75, 0.375), # Ab3
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Diane (piano) - comping on 2 and 4
piano_notes = [
    (62, 4.875, 0.375), # F#4 (F7)
    (65, 4.875, 0.375), # A4 (F7)
    (67, 4.875, 0.375), # B4 (F7)
    (69, 4.875, 0.375), # C#5 (F7)
    (62, 6.0, 0.375), # F#4 (F7)
    (65, 6.0, 0.375), # A4 (F7)
    (67, 6.0, 0.375), # B4 (F7)
    (69, 6.0, 0.375), # C#5 (F7)
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Dante (sax) - motif
sax_notes = [
    (66, 4.5, 0.375), # F4
    (68, 4.875, 0.375), # G4
    (69, 5.25, 0.375), # A4
    (66, 5.625, 0.375), # F4
    (66, 6.0, 0.375), # F4
    (68, 6.375, 0.375), # G4
    (69, 6.75, 0.375), # A4
    (66, 7.125, 0.375), # F4
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
