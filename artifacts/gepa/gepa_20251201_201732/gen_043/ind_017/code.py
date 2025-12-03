
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), chromatic approach to G2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=39, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25),
    # Bar 3: G2 (fifth), chromatic approach to A2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),
    # Bar 4: A2 (chromatic), resolve to D2
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=75, pitch=69, start=1.5, end=1.875),  # C#4
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=85, pitch=71, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=75, pitch=74, start=2.25, end=2.625),  # F5
    # Bar 4: A7sus4 (A, D, E, G)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=85, pitch=76, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=80, pitch=77, start=3.0, end=3.375),  # E5
    pretty_midi.Note(velocity=75, pitch=74, start=3.0, end=3.375),  # G5
]
piano.notes.extend(piano_notes)

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - A4 - B4 (Dorian mode)
# First phrase: 1.5 - 2.25s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25),  # A4
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),  # A4
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(bar_start, bar_duration):
    kick_start = bar_start
    snare_start = bar_start + 0.75
    hihat_start = bar_start
    for i in range(4):
        kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_start + i*0.375, end=kick_start + i*0.375 + 0.375)
        drums.notes.append(kick)
        snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_start + i*0.375, end=snare_start + i*0.375 + 0.375)
        drums.notes.append(snare)
        for j in range(4):
            hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_start + j*0.1875, end=hihat_start + j*0.1875 + 0.1875)
            drums.notes.append(hihat)
    return bar_start + bar_duration

# Bar 2
add_drums(1.5, 1.5)
# Bar 3
add_drums(3.0, 1.5)
# Bar 4
add_drums(4.5, 1.5)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
