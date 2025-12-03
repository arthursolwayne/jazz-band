
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), F#2 (fifth), chromatic approach to G2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=41, start=1.625, end=1.75),
    pretty_midi.Note(velocity=90, pitch=42, start=1.75, end=1.875),
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.0),
    # Bar 3: G2 (root), B2 (fifth), chromatic approach to A2
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=46, start=2.125, end=2.25),
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=44, start=2.375, end=2.5),
    # Bar 4: A2 (root), C#3 (fifth), chromatic approach to B2
    pretty_midi.Note(velocity=90, pitch=44, start=2.5, end=2.625),
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=47, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=46, start=2.875, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: C7 (F7) - open voicing
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),
    # Bar 3: G7 - open voicing
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.25),
    # Bar 4: Am7 - open voicing
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=79, start=2.5, end=2.75)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),
    # Bar 3: Continue motif
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),
    # Bar 4: Resolve motif
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),
    pretty_midi.Note(velocity=110, pitch=60, start=2.75, end=3.0)
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3
for bar in [0, 1, 2]:
    kick_start = 1.5 + bar * 1.5
    kick_end = kick_start + 0.375
    kick_start_3 = kick_start + 1.125
    kick_end_3 = kick_start_3 + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start_3, end=kick_end_3))

# Snare on 2 and 4
for bar in [0, 1, 2]:
    snare_start = 1.5 + bar * 1.5 + 0.75
    snare_end = snare_start + 0.125
    snare_start_4 = snare_start + 1.5
    snare_end_4 = snare_start_4 + 0.125
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end))
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start_4, end=snare_end_4))

# Hihat on every eighth
for bar in [0, 1, 2]:
    for eighth in range(8):
        start = 1.5 + bar * 1.5 + eighth * 0.375
        end = start + 0.1875
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
