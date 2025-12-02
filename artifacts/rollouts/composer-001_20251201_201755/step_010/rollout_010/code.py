
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
drums_notes = [
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
]

for note in drums_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in F, roots and fifths with chromatic approaches
# F (F2), C (C3), G (G2), D (D3), A (A2), E (E3), B (B2), F# (F#2), etc.
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),   # F2 (root)
    pretty_midi.Note(velocity=80, pitch=76, start=1.875, end=2.25),  # C3 (fifth)
    pretty_midi.Note(velocity=80, pitch=70, start=2.25, end=2.625),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=74, start=2.625, end=3.0),   # D3 (root)
    pretty_midi.Note(velocity=80, pitch=77, start=3.0, end=3.375),   # A2 (fifth)
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75),  # E3 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=4.125),  # A2 (root)
    pretty_midi.Note(velocity=80, pitch=79, start=4.125, end=4.5),   # E3 (fifth)
    pretty_midi.Note(velocity=80, pitch=73, start=4.5, end=4.875),   # B2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=77, start=4.875, end=5.25),  # F#2 (root)
    pretty_midi.Note(velocity=80, pitch=80, start=5.25, end=5.625),  # C#3 (fifth)
    pretty_midi.Note(velocity=80, pitch=75, start=5.625, end=6.0),   # G2 (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # E

    # Bar 3: Bm7 (B, D, F#, A)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A

    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F

    # Bar 4: Resolve to Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): one short motif, make it sing
# F (F4), A (A4), C (C5), F (F4) — motif with space and tension
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=77, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=81, start=2.25, end=2.625),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # F4 (resolution)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75),
    # Hihat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + (i + 1) * 0.375),
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875),

# Add all instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
