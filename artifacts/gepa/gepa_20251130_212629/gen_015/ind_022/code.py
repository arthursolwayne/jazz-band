
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
kick = 36
snare = 38
hihat = 42

# Bar 1 (0.0 - 1.5s): Little Ray alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [0]:
    for beat in [0, 2]:  # Kick on 1 and 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=bar * 1.5 + beat * 0.375, end=bar * 1.5 + beat * 0.375 + 0.125))
    for beat in [1, 3]:  # Snare on 2 and 4
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=bar * 1.5 + beat * 0.375, end=bar * 1.5 + beat * 0.375 + 0.125))
    for eighth in range(8):  # Hihat on every eighth
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=bar * 1.5 + eighth * 0.1875, end=bar * 1.5 + eighth * 0.1875 + 0.0625))

# Bar 2 (1.5 - 3.0s): Full quartet
# Bass: Walking line in F minor, chromatic approaches
# Start on F, walk down chromatically to E♭, then up to G, to A♭, then resolve to F
bass_notes = [
    pretty_midi.Note(velocity=85, pitch=71, start=1.5, end=1.5 + 0.375),  # F (71)
    pretty_midi.Note(velocity=85, pitch=70, start=1.875, end=1.875 + 0.375),  # E♭ (70)
    pretty_midi.Note(velocity=85, pitch=72, start=2.25, end=2.25 + 0.375),  # G (72)
    pretty_midi.Note(velocity=85, pitch=71, start=2.625, end=2.625 + 0.375),  # F (71)
    pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=3.0 + 0.1875)  # A♭ (69) - held
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# F7 on 2, B♭7 on 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E♭) on beat 2
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=1.875 + 0.1875),
    pretty_midi.Note(velocity=80, pitch=74, start=1.875, end=1.875 + 0.1875),
    pretty_midi.Note(velocity=80, pitch=76, start=1.875, end=1.875 + 0.1875),
    pretty_midi.Note(velocity=80, pitch=70, start=1.875, end=1.875 + 0.1875),
    # Bar 2: B♭7 (B♭, D, F, A♭) on beat 4
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=2.625 + 0.1875),
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=2.625 + 0.1875),
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=2.625 + 0.1875),
    pretty_midi.Note(velocity=80, pitch=74, start=2.625, end=2.625 + 0.1875),
]
piano.notes.extend(piano_notes)

# Drums: Continue with kick, snare, hihat
for bar in [1]:
    for beat in [0, 2]:  # Kick on 1 and 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=bar * 1.5 + beat * 0.375, end=bar * 1.5 + beat * 0.375 + 0.125))
    for beat in [1, 3]:  # Snare on 2 and 4
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=bar * 1.5 + beat * 0.375, end=bar * 1.5 + beat * 0.375 + 0.125))
    for eighth in range(8):  # Hihat on every eighth
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=bar * 1.5 + eighth * 0.1875, end=bar * 1.5 + eighth * 0.1875 + 0.0625))

# Bar 3 (3.0 - 4.5s): Sax takes the melody
# Motif: F (72), G (72), A♭ (71), F (72) — resolved on the last bar
# Start it, leave it hanging, then finish it
sax_notes = [
    # Bar 2: F (72), held for the first half of the bar
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.875),
    # Bar 2: G (72) on beat 2
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=1.875 + 0.1875),
    # Bar 2: A♭ (71) on beat 3 (half note, held)
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),
    # Bar 3: F (72) on beat 4 (half note, held)
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=3.0)
]
sax.notes.extend(sax_notes)

# Bar 4 (4.5 - 6.0s): Full ensemble, repeat motif with variation
# Sax takes it again, now with a slight variation: A♭ (71) -> G (72) -> F (72)
sax_notes = [
    # Bar 3: A♭ (71) on beat 1
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.0 + 0.1875),
    # Bar 3: G (72) on beat 2
    pretty_midi.Note(velocity=110, pitch=72, start=3.375, end=3.375 + 0.1875),
    # Bar 3: F (72) on beat 3 (half note, held)
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.125),
    # Bar 4: G (72) on beat 4 (half note, held)
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=5.0)
]
sax.notes.extend(sax_notes)

# Drum fill in bar 3 (4.5s)
for bar in [2]:
    for beat in [0, 2]:  # Kick on 1 and 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=bar * 1.5 + beat * 0.375, end=bar * 1.5 + beat * 0.375 + 0.125))
    for beat in [1, 3]:  # Snare on 2 and 4
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=bar * 1.5 + beat * 0.375, end=bar * 1.5 + beat * 0.375 + 0.125))
    for eighth in range(8):  # Hihat on every eighth
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=bar * 1.5 + eighth * 0.1875, end=bar * 1.5 + eighth * 0.1875 + 0.0625))

# Bass: walking line again, F minor
bass_notes = [
    pretty_midi.Note(velocity=85, pitch=71, start=3.0, end=3.0 + 0.375),  # F
    pretty_midi.Note(velocity=85, pitch=70, start=3.375, end=3.375 + 0.375),  # E♭
    pretty_midi.Note(velocity=85, pitch=72, start=3.75, end=3.75 + 0.375),  # G
    pretty_midi.Note(velocity=85, pitch=71, start=4.125, end=4.125 + 0.375),  # F
    pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=4.5 + 0.1875)  # A♭
]
bass.notes.extend(bass_notes)

# Piano: F7 on beat 2, D7 on beat 4
piano_notes = [
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.375 + 0.1875),
    pretty_midi.Note(velocity=80, pitch=74, start=3.375, end=3.375 + 0.1875),
    pretty_midi.Note(velocity=80, pitch=76, start=3.375, end=3.375 + 0.1875),
    pretty_midi.Note(velocity=80, pitch=70, start=3.375, end=3.375 + 0.1875),
    # Bar 4: D7 (D, F#, A, C) on beat 4
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.5 + 0.1875),
    pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.5 + 0.1875),
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.5 + 0.1875),
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.5 + 0.1875),
]
piano.notes.extend(piano_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
