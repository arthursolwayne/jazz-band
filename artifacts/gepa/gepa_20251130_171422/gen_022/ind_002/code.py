
import pretty_midi

# Initialize the MIDI file with the specified tempo (160 BPM)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for each player
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42

# ============ BAR 1: DRUMS ONLY (0.0 - 1.5s) ============
# A question, deliberate space, and an inquisitive pulse
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
    
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),  # OUT OF BOUNDS (only 1.5s in this bar)
    
    # Hihat on every eighth note
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5)
]

drums.notes.extend(drum_notes)

# ============ BAR 2-4: FULL QUARTET (1.5 - 6.0s) ============

# ============ DRUMS (1.5 - 6.0s) ============
for i in range(3):  # 3 bars
    start = 1.5 + i * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=80, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=80, pitch=36, start=start + 0.75, end=start + 1.125)
    
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=90, pitch=38, start=start + 1.125, end=start + 1.5)
    
    # Hihat on every eighth note
    for j in range(4):
        pretty_midi.Note(velocity=60, pitch=42, start=start + j * 0.375, end=start + j * 0.375 + 0.375)

drums.notes.extend([note for note in drums.notes if note.start >= 1.5])  # Only keep bar 2-4

# ============ BASS (1.5 - 6.0s) ============
# Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=2.625, end=3.0),   # E

    # Bar 3
    pretty_midi.Note(velocity=80, pitch=46, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),   # A

    # Bar 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=80, pitch=45, start=5.625, end=6.0),   # D
]

bass.notes.extend(bass_notes)

# ============ PIANO (1.5 - 6.0s) ============
# 7th chords, comp on 2 and 4. Keep it moving, out of the way
piano_notes = [
    # Bar 2
    # Chord on 2 and 4 (F7)
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=68, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),  # G

    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=80, pitch=68, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),   # G

    # Bar 3
    # Chord on 2 and 4 (Gm7)
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # D

    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),   # D

    # Bar 4
    # Chord on 2 and 4 (Cm7)
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),  # D

    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),   # C
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),   # E
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),   # D
]

piano.notes.extend(piano_notes)

# ============ SAX (1.5 - 6.0s) ============
# Your motif: a short, emotionally charged melody. Start it, leave it hanging, come back.
# Melody is in Fm, with a hint of tension and resolution
sax_notes = [
    # Bar 2 (start on 1)
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),   # F#

    # Bar 3 (rests, space, then a variation)
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),   # E

    # Bar 4 (resolve the tension)
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # E
]

sax.notes.extend(sax_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("fm_intro.mid")
