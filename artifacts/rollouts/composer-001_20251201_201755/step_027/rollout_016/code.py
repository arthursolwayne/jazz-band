
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Fm (F2, Bb2, Eb2, Ab2 with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625),  # Gb2 (Bb2)
    pretty_midi.Note(velocity=100, pitch=79, start=2.625, end=3.0),  # Ab2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=80, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=3.0),  # Eb
]
piano.notes.extend(piano_notes)

# Bar 2: Sax motif (start on F, leave it hanging)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=82, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=110, pitch=77, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=82, start=2.25, end=2.5),  # Eb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in Fm (F2, Bb2, Eb2, Ab2 with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.125),  # Gb2 (Bb2)
    pretty_midi.Note(velocity=100, pitch=79, start=4.125, end=4.5),  # Ab2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=4.5),  # Ab
]
piano.notes.extend(piano_notes)

# Bar 3: Sax motif (continue the motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=82, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=110, pitch=77, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=82, start=3.75, end=4.0),  # Eb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in Fm (F2, Bb2, Eb2, Ab2 with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.625),  # Gb2 (Bb2)
    pretty_midi.Note(velocity=100, pitch=79, start=5.625, end=6.0),  # Ab2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=80, start=4.5, end=6.0),  # Bb
]
piano.notes.extend(piano_notes)

# Bar 4: Sax motif (finish the motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=82, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=110, pitch=77, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=82, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=110, pitch=77, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=110, pitch=82, start=5.75, end=6.0),  # Eb
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
for i in range(4):
    kick_start = 1.5 + i * 0.75
    snare_start = 1.5 + i * 0.75 + 0.375
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375),
        pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_start + 0.125),
    ]
    for j in range(8):
        hihat_start = 1.5 + i * 0.75 + j * 0.1875
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_start + 0.1875))
    drums.notes.extend(drum_notes)

# Bar 3 (3.0 - 4.5s)
for i in range(4):
    kick_start = 3.0 + i * 0.75
    snare_start = 3.0 + i * 0.75 + 0.375
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375),
        pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_start + 0.125),
    ]
    for j in range(8):
        hihat_start = 3.0 + i * 0.75 + j * 0.1875
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_start + 0.1875))
    drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
for i in range(4):
    kick_start = 4.5 + i * 0.75
    snare_start = 4.5 + i * 0.75 + 0.375
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375),
        pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_start + 0.125),
    ]
    for j in range(8):
        hihat_start = 4.5 + i * 0.75 + j * 0.1875
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_start + 0.1875))
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
