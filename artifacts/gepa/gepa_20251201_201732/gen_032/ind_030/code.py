
import pretty_midi

# Initialize MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante on tenor sax
bass = pretty_midi.Instrument(program=33)      # Marcus on bass
piano = pretty_midi.Instrument(program=0)      # Diane on piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray on drums

# Drum note numbers
kick = 36
snare = 38
hihat = 42

# Time per bar is 1.5 seconds (160 BPM, 4/4 time)
bar_length = 1.5

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * bar_length + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125))
        for eighth in range(2):
            hihat_time = time + eighth * 0.1875
            drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=hihat_time, end=hihat_time + 0.0625))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line in D (D2-G2), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), F#2 (chromatic approach to G2), G2 (fifth), F#2 (approach to D2)
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=80, pitch=41, start=1.5 + 0.375, end=1.5 + 0.75),
    pretty_midi.Note(velocity=80, pitch=43, start=1.5 + 0.75, end=1.5 + 1.125),
    pretty_midi.Note(velocity=80, pitch=41, start=1.5 + 1.125, end=1.5 + 1.5),
    
    # Bar 3: G2 (fifth), A2 (chromatic), B2 (root), A2 (approach to G2)
    pretty_midi.Note(velocity=80, pitch=43, start=1.5 + 1.5, end=1.5 + 1.875),
    pretty_midi.Note(velocity=80, pitch=44, start=1.5 + 1.875, end=1.5 + 2.25),
    pretty_midi.Note(velocity=80, pitch=45, start=1.5 + 2.25, end=1.5 + 2.625),
    pretty_midi.Note(velocity=80, pitch=44, start=1.5 + 2.625, end=1.5 + 3.0),
    
    # Bar 4: D2 (root), E2 (chromatic), F#2 (fifth), E2 (approach to D2)
    pretty_midi.Note(velocity=80, pitch=43, start=1.5 + 3.0, end=1.5 + 3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5 + 3.375, end=1.5 + 3.75),
    pretty_midi.Note(velocity=80, pitch=41, start=1.5 + 3.75, end=1.5 + 4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5 + 4.125, end=1.5 + 4.5),
]

bass.notes.extend(bass_notes)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#) - open voicing on beat 2
piano.notes.append(pretty_midi.Note(velocity=85, pitch=62, start=1.5 + 0.75, end=1.5 + 1.125))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=64, start=1.5 + 0.75, end=1.5 + 1.125))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=1.5 + 0.75, end=1.5 + 1.125))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.5 + 0.75, end=1.5 + 1.125))

# Bar 3: Gm7 (G, Bb, D, F) - open voicing on beat 2
piano.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=1.5 + 2.25, end=1.5 + 2.625))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=1.5 + 2.25, end=1.5 + 2.625))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=1.5 + 2.25, end=1.5 + 2.625))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.5 + 2.25, end=1.5 + 2.625))

# Bar 4: Cmaj7 (C, E, G, B) - open voicing on beat 2
piano.notes.append(pretty_midi.Note(velocity=85, pitch=60, start=1.5 + 3.75, end=1.5 + 4.125))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=64, start=1.5 + 3.75, end=1.5 + 4.125))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.5 + 3.75, end=1.5 + 4.125))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=1.5 + 3.75, end=1.5 + 4.125))

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D - F# - E - D (but played with a little space and tension)

# Bar 2: D (start), F# (beat 2)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 0.75, end=1.5 + 1.125))

# Bar 3: E (beat 1), D (beat 2)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5 + 1.5, end=1.5 + 1.875))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 2.25, end=1.5 + 2.625))

# Bar 4: Repeat the motif (D - F# - E - D)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 3.0, end=1.5 + 3.375))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 3.75, end=1.5 + 4.125))

# Add the full quartet to the MIDI file
midi.instruments.append(sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Save the MIDI file
# midi.write disabled
