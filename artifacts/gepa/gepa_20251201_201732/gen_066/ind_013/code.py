
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
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
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass - D2 (MIDI 38) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),    # D2
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25),   # Eb2
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625),   # E2
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),    # F2
]
bass.notes.extend(bass_notes)

# Piano - open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),   # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),   # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),   # A4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),   # C5
]
piano.notes.extend(piano_notes)

# Sax - motif: D4 - E4 - F4 - D4 (half note on beat 1, quarter on beat 2)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),   # D4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),   # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass - G2 (MIDI 43) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),    # G2
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75),   # Ab2
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125),   # A2
    pretty_midi.Note(velocity=90, pitch=46, start=4.125, end=4.5),    # Bb2
]
bass.notes.extend(bass_notes)

# Piano - Bb7 (Bb D F Ab)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),   # Bb4
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),   # D5
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),   # F5
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375),   # Ab5
]
piano.notes.extend(piano_notes)

# Sax - motif: Bb4 - C4 - D4 - Bb4 (half note on beat 1, quarter on beat 2)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.75),   # Bb4
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # D4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass - C2 (MIDI 36) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),    # C2
    pretty_midi.Note(velocity=90, pitch=37, start=4.875, end=5.25),   # C#2
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625),   # D2
    pretty_midi.Note(velocity=90, pitch=39, start=5.625, end=6.0),    # Eb2
]
bass.notes.extend(bass_notes)

# Piano - Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),   # D4
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),   # F4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),   # A4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),   # C5
]
piano.notes.extend(piano_notes)

# Sax - motif: D4 - E4 - F4 - D4 (half note on beat 1, quarter on beat 2)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.25),   # D4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),   # F4
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Kick on 1 and 3
for bar in range(2, 4):
    kick_start = 1.5 + bar * 1.5
    kick_end = kick_start + 0.375
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    kick_start = 1.5 + bar * 1.5 + 1.125
    kick_end = kick_start + 0.375
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))

# Snare on 2 and 4
for bar in range(2, 4):
    snare_start = 1.5 + bar * 1.5 + 0.75
    snare_end = snare_start + 0.375
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end))
    snare_start = 1.5 + bar * 1.5 + 1.875
    snare_end = snare_start + 0.375
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end))

# Hi-hat on every eighth
for bar in range(2, 4):
    hihat_start = 1.5 + bar * 1.5
    for i in range(4):
        hihat_end = hihat_start + 0.375
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end))
        hihat_start += 0.375

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
