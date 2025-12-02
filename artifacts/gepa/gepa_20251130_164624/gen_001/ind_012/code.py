
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in D, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # E
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # B
    pretty_midi.Note(velocity=90, pitch=65, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),  # E
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=90, pitch=65, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # D7: D, F#, A, C
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Short motif, sing it, leave it hanging, come back
# Start at 1.5s (Bar 2), play motif, leave it hanging at 3.0s, come back at 4.5s
sax_notes = [
    # First motif
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # B
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=110, pitch=68, start=2.25, end=2.5),  # D#
    # Leave it hanging (no note at 2.5-3.0)
    # Return at 4.5s
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),  # B
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=68, start=5.25, end=5.5),  # D#
    # End with a strong note
    pretty_midi.Note(velocity=110, pitch=71, start=5.5, end=5.75),  # F#
    pretty_midi.Note(velocity=110, pitch=69, start=5.75, end=6.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: continue in bars 2-4
# Kick on 1 and 3
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    kick_start = start + 0.0
    kick_end = kick_start + 0.375
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    drums.notes.append(kick_note)

    kick_start = start + 1.125
    kick_end = kick_start + 0.375
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    drums.notes.append(kick_note)

    # Snare on 2 and 4
    snare_start = start + 0.75
    snare_end = snare_start + 0.125
    snare_note = pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end)
    drums.notes.append(snare_note)

    snare_start = start + 1.875
    snare_end = snare_start + 0.125
    snare_note = pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end)
    drums.notes.append(snare_note)

    # Hihat on every eighth
    for i in range(8):
        hihat_start = start + (i * 0.1875)
        hihat_end = hihat_start + 0.1875
        hihat_note = pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end)
        drums.notes.append(hihat_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
