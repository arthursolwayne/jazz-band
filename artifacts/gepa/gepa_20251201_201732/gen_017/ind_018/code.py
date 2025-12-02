
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Fm root (F), root and fifth with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicing - Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=46, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=44, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=110, pitch=46, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=43, start=2.625, end=3.0),   # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Fm root (F), root and fifth with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=39, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicing - Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=46, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=44, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=110, pitch=46, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=110, pitch=43, start=4.125, end=4.5),   # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Fm root (F), root and fifth with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=39, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicing - Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=46, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=44, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=110, pitch=46, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=43, start=5.625, end=6.0),   # F
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3
for bar in range(2, 5):
    kick_start = bar * 1.5
    kick_end = kick_start + 0.375
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    kick_start = kick_start + 1.125
    kick_end = kick_start + 0.375
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))

# Snare on 2 and 4
for bar in range(2, 5):
    snare_start = bar * 1.5 + 0.75
    snare_end = snare_start + 0.125
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    snare_start = snare_start + 1.5
    snare_end = snare_start + 0.125
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))

# Hi-hat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(4):
        hihat_start = start + i * 0.375
        hihat_end = hihat_start + 0.125
        sax.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
