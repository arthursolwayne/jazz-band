
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
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=1.125), # Hihat on 2 and 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3 and 4
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=2.0),  # F (root)
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.5),  # C (fifth)
    pretty_midi.Note(velocity=80, pitch=40, start=2.5, end=3.0),  # Bb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.5),  # D (next root)
    pretty_midi.Note(velocity=80, pitch=39, start=3.5, end=4.0),  # Eb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=4.0, end=4.5),  # D (root)
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.0),  # C (fifth)
    pretty_midi.Note(velocity=80, pitch=40, start=5.0, end=5.5),  # Bb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=5.5, end=6.0),  # F (root)
]
for note in bass_notes:
    bass.notes.append(note)

# Diane - Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F A C Eb) - open voicings
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F (4th octave)
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # Eb

    # Bar 3: Bb7 (Bb D F Ab) - open voicings
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.5),  # Ab

    # Bar 4: Eb7 (Eb G Bb D) - open voicings
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),  # D (chromatic approach)

    # Bar 2 (1.5-2.0) resolves on last chord
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C (resolve)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # Eb (resolve)
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=2.0),  # A (resolve)

    # Bar 3 (2.0-2.5)
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # F (resolve)
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.5),  # Bb (resolve)
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # D (resolve)

    # Bar 4 (2.5-3.0)
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0),  # Bb (resolve)
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=3.0),  # Eb (resolve)
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),  # G (resolve)
]
for note in piano_notes:
    piano.notes.append(note)

# Dante - Tenor sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Motif intro
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),   # Bb

    # Bar 3: Return with variation
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.625, end=3.875), # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.0),  # Bb

    # Bar 4: Resolve with a touch of tension
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),   # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = (bar - 1) * 1.5
    # Bar 2
    if bar == 2:
        kick_start = start_time
        kick_end = kick_start + 0.375
        snare_start = start_time + 0.75
        snare_end = snare_start + 0.375
        hihat_start = start_time + 0.375
        hihat_end = hihat_start + 0.375
        hihat2_start = start_time + 0.75
        hihat2_end = hihat2_start + 0.375
        hihat3_start = start_time + 1.125
        hihat3_end = hihat3_start + 0.375
        hihat4_start = start_time + 1.5
        hihat4_end = hihat4_start + 0.375

        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat2_start, end=hihat2_end))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat3_start, end=hihat3_end))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat4_start, end=hihat4_end))

    # Bar 3
    if bar == 3:
        kick_start = start_time
        kick_end = kick_start + 0.375
        snare_start = start_time + 0.75
        snare_end = snare_start + 0.375
        hihat_start = start_time + 0.375
        hihat_end = hihat_start + 0.375
        hihat2_start = start_time + 0.75
        hihat2_end = hihat2_start + 0.375
        hihat3_start = start_time + 1.125
        hihat3_end = hihat3_start + 0.375
        hihat4_start = start_time + 1.5
        hihat4_end = hihat4_start + 0.375

        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat2_start, end=hihat2_end))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat3_start, end=hihat3_end))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat4_start, end=hihat4_end))

    # Bar 4
    if bar == 4:
        kick_start = start_time
        kick_end = kick_start + 0.375
        snare_start = start_time + 0.75
        snare_end = snare_start + 0.375
        hihat_start = start_time + 0.375
        hihat_end = hihat_start + 0.375
        hihat2_start = start_time + 0.75
        hihat2_end = hihat2_start + 0.375
        hihat3_start = start_time + 1.125
        hihat3_end = hihat3_start + 0.375
        hihat4_start = start_time + 1.5
        hihat4_end = hihat4_start + 0.375

        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat2_start, end=hihat2_end))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat3_start, end=hihat3_end))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat4_start, end=hihat4_end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
